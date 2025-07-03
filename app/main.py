from fastapi import FastAPI, Query
from app.excel_utils import get_excel_tables, get_table_details, get_row_sum
from app.llm_utils import ask_question

app = FastAPI()

@app.get("/list_tables")
def list_tables():
    return {"tables": get_excel_tables()}

@app.get("/get_table_details")
def get_details(table_name: str = Query(...)):
    return get_table_details(table_name)

@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    return get_row_sum(table_name, row_name)

@app.get("/ask")
def ask(prompt: str = Query(...)):
    return ask_question(prompt)
