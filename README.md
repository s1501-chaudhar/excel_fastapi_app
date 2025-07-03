
# 🧾 Excel Data API

This project exposes RESTful APIs to extract, summarize, and inspect data from Excel files, primarily for capital budgeting analysis.

---

## 📌 Endpoints

### `GET /list_tables`

Returns a list of available Excel sheet names (or logical tables if implemented).

**Response**

```json
{
  "tables": ["Initial Investment", "Revenue Projections", "Operating Expenses"]
}
```

---

### `GET /get_table_details?table_name=<TABLE_NAME>`

Returns all row labels (typically from the first column) for the given table/sheet.

**Example**

```http
GET /get_table_details?table_name=Initial Investment
```

**Response**

```json
{
  "table_name": "Initial Investment",
  "row_names": [
    "Initial Investment=",
    "Opportunity cost (if any)=",
    "Lifetime of the investment",
    "Salvage Value at end of project=",
    "Deprec. method(1:St.line;2:DDB)=",
    "Tax Credit (if any )=",
    "Other invest.(non-depreciable)="
  ]
}
```

---

### `GET /row_sum?table_name=<TABLE_NAME>&row_name=<ROW_NAME>`

Returns the sum of numeric values in the specified row across columns.

**Example**

```http
GET /row_sum?table_name=Initial Investment&row_name=Tax Credit (if any )=
```

**Response**

```json
{
  "table_name": "Initial Investment",
  "row_name": "Tax Credit (if any )=",
  "sum": 10
}
```

---

## 📂 Postman Collection

A complete Postman collection with sample requests and example responses is included in this repo:
📁 `ExcelAPI.postman_collection.json`
*Import into Postman to test all endpoints easily.*

---

## 💡 Your Insights

### ✅ Potential Improvements

1. **Multi-format Excel Support**
   Add compatibility for `.xlsx`, `.xlsm`, `.ods` using `openpyxl` and `pyxlsb`.

2. **Logical Table Extraction from One Sheet**
   Add logic to extract named sections from a single sheet by detecting titles or separators (e.g., bolded headers or merged cells).

3. **Advanced Data Aggregations**
   Include endpoints like:

   * Column-wise stats (mean, std, count)
   * `GET /search_rows?contains=investment` to filter by keywords

4. **UI Integration**
   A front-end interface (via Streamlit or React) could allow users to upload Excel files and view sheet data interactively.

5. **File Upload Endpoint**
   A POST endpoint to upload Excel files via API, storing them temporarily or persistently.

---

### ⚠️ Missed Edge Cases

* **Empty or Malformed Excel Files** – Could return no response or crash.
* **Duplicate Row Names** – The API doesn't clarify which one was summed.
* **Non-Numeric Row Values** – Mixed or invalid types could silently fail.
* **Case Sensitivity** – `Initial Investment` ≠ `initial investment` unless normalized.
* **Whitespace Sensitivity** – Rows with extra spaces won't match unless trimmed.
* **No Table Name Provided** – Currently results in `422 Unprocessable Entity` errors.

---

## 🧑‍💻 Developer Notes

### Folder Structure

```
├── main.py                 # FastAPI app
├── excel_utils.py          # Sheet parsing, row extraction logic
├── sample.xls              # Example Excel used for testing
├── README.md               # Documentation
├── ExcelAPI.postman_collection.json  # Postman test cases
```

### Code Documentation

* Functions and endpoints are fully annotated with docstrings.
* Uses type hints (`str`, `List[str]`, etc.) to ensure clarity.
* Error handling for common request issues is implemented.
