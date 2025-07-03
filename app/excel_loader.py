import pandas as pd
from .config import EXCEL_FILE_PATH

def load_excel_sheets():
    xls = pd.ExcelFile(EXCEL_FILE_PATH)
    sheets = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
    return sheets
