import pandas as pd

EXCEL_PATH = "C:\\Environments\\GenAi_test\\Data\\capbudg.xls"
sheet_name = "CapBudgWS"
df = pd.read_excel(EXCEL_PATH, sheet_name=sheet_name, header=None)

def get_excel_tables():
    # Simulate multiple table extraction
    return ["Initial Investment", "Revenue Projections", "Operating Expenses"]

def get_table_details(table_name: str):
    tables = {
        "Initial Investment": [
            "Initial Investment=",
            "Opportunity cost (if any)=",
            "Lifetime of the investment",
            "Salvage Value at end of project=",
            "Deprec. method(1:St.line;2:DDB)=",
            "Tax Credit (if any )=",
            "Other invest.(non-depreciable)="
        ]
    }
    return {"table_name": table_name, "row_names": tables.get(table_name, [])}

def get_row_sum(table_name: str, row_name: str):
    if table_name == "Initial Investment":
        # Dummy mapping
        mapping = {
            "Tax Credit (if any )=": 10
        }
        return {"table_name": table_name, "row_name": row_name, "sum": mapping.get(row_name, 0)}
    return {"table_name": table_name, "row_name": row_name, "sum": 0}

