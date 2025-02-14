Real-world code examples for each of the bad practices mentioned, along with proper alternatives.

---

### 1. **Loading entire datasets into memory when it’s not necessary**
**Bad Practice: Reading a large CSV into Pandas and running `.head()`**
```python
import pandas as pd

df = pd.read_csv("large_dataset.csv")  # Loads entire file into memory
print(df.head())  
```
✅ **Better Alternative: Use `chunksize` to read in chunks**
```python
chunk_size = 10000  # Process data in chunks
for chunk in pd.read_csv("large_dataset.csv", chunksize=chunk_size):
    print(chunk.head())  # Process each chunk separately
```

---

### 2. **Overengineering ETL pipelines for simple tasks**
**Bad Practice: Using Airflow and a full pipeline for a simple CSV transformation**
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def transform_data():
    df = pd.read_csv("data.csv")
    df["new_col"] = df["existing_col"] * 2
    df.to_csv("transformed_data.csv", index=False)

dag = DAG("overengineered_pipeline", start_date=datetime(2024, 2, 1), schedule_interval="@daily")

task = PythonOperator(task_id="transform_task", python_callable=transform_data, dag=dag)
```
✅ **Better Alternative: A simple Python script**
```python
import pandas as pd

df = pd.read_csv("data.csv")
df["new_col"] = df["existing_col"] * 2
df.to_csv("transformed_data.csv", index=False)
```

---

### 3. **Using Excel as a database**
**Bad Practice: Reading an Excel file multiple times and performing operations manually**
```python
df = pd.read_excel("data.xlsx")
filtered_df = df[df["status"] == "active"]
filtered_df.to_excel("filtered_data.xlsx", index=False)
```
✅ **Better Alternative: Store in SQLite and query efficiently**
```python
import sqlite3

conn = sqlite3.connect("database.db")
df = pd.read_excel("data.xlsx")
df.to_sql("users", conn, if_exists="replace", index=False)

# Query instead of filtering manually
query_result = pd.read_sql("SELECT * FROM users WHERE status = 'active'", conn)
query_result.to_csv("filtered_data.csv", index=False)
```

---

### 4. **Ignoring SQL performance optimization**
**Bad Practice: Using `SELECT *` unnecessarily**
```sql
SELECT * FROM orders;
```
✅ **Better Alternative: Select only required columns**
```sql
SELECT order_id, customer_name, total_amount FROM orders;
```

---

### 5. **Using JSON fields in SQL as a crutch**
**Bad Practice: Extracting JSON fields in every query**
```sql
SELECT data->>'customer_name' AS customer_name FROM orders;
```
✅ **Better Alternative: Normalize your schema**
```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name TEXT
);
```
And reference it properly:
```sql
SELECT customers.customer_name FROM customers JOIN orders ON customers.customer_id = orders.customer_id;
```

---

### 6. **Not version-controlling data transformations**
**Bad Practice: Keeping transformations in Jupyter notebooks only**
```python
df["new_col"] = df["old_col"] * 2  # Transforms data manually each time
```
✅ **Better Alternative: Store transformations in a version-controlled script**
```bash
git init
git add transform.py
git commit -m "Initial commit for transformation script"
```
Then in `transform.py`:
```python
import pandas as pd

def transform_data(df):
    df["new_col"] = df["old_col"] * 2
    return df
```

---

### 7. **Not documenting anything**
**Bad Practice: Writing SQL queries with zero comments**
```sql
SELECT order_id, total_amount FROM orders WHERE status = 'shipped';
```
✅ **Better Alternative: Comment your queries**
```sql
-- Fetch shipped orders along with their total amount
SELECT order_id, total_amount FROM orders WHERE status = 'shipped';
```

---

### 8. **Using row-based processing instead of vectorized operations**
**Bad Practice: Iterating over DataFrame rows**
```python
for index, row in df.iterrows():
    df.at[index, "new_col"] = row["old_col"] * 2
```
✅ **Better Alternative: Use vectorized operations**
```python
df["new_col"] = df["old_col"] * 2  # Runs much faster
```

---

### 9. **Ignoring nulls and data integrity issues**
**Bad Practice: Assuming all data is clean**
```python
df = pd.read_csv("data.csv")
df["price"] = df["price"].astype(float)  # This will fail if price has nulls
```
✅ **Better Alternative: Handle missing data properly**
```python
df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
```

---

### 10. **Thinking “we’ll fix it in the dashboard”**
**Bad Practice: Hardcoding fixes in Tableau or Power BI**
```sql
CASE WHEN country = 'US' THEN 'United States' ELSE country END AS normalized_country
```
✅ **Better Alternative: Fix it in the source**
```sql
UPDATE customers SET country = 'United States' WHERE country = 'US';
```

---

### 11. **Overcomplicating machine learning models**
**Bad Practice: Using deep learning when a rule-based approach is enough**
```python
from tensorflow import keras

model = keras.Sequential([...])  # Overkill for a simple classification task
```
✅ **Better Alternative: Use simple heuristics if applicable**
```python
df["is_fraud"] = df["transaction_amount"] > 10000  # Simple rule-based detection
```

---
