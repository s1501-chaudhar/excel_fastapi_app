from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .excel_loader import load_excel_sheets

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tables = {}

@app.on_event("startup")
def startup_event():
    global tables
    tables = load_excel_sheets()

@app.get("/list_tables")
def list_tables():
    return {"tables": list(tables.keys())}

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    if table_name not in tables:
        raise HTTPException(status_code=404, detail="Table not found")
    df = tables[table_name]
    first_column = df.iloc[:, 0].dropna().astype(str).tolist()
    return {"table_name": table_name, "row_names": first_column}

@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    if table_name not in tables:
        raise HTTPException(status_code=404, detail="Table not found")
    df = tables[table_name].dropna(how="all")
    row = df[df.iloc[:, 0].astype(str) == row_name]
    if row.empty:
        raise HTTPException(status_code=404, detail="Row not found")
    numerical_values = row.iloc[0, 1:].apply(pd.to_numeric, errors="coerce").dropna()
    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": numerical_values.sum()
    }
