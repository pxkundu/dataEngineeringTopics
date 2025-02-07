### **Preferred Methods for Data Quality Testing and Validation**  

Ensuring **data quality** is critical in **ETL pipelines, analytics, and reporting**. Below is a structured approach to **data quality testing and validation**, covering best practices, tools, and techniques.

---

## **🔹 1. Key Aspects of Data Quality Testing**
✅ **Accuracy** – Is the data correct compared to the source?  
✅ **Completeness** – Are all required records present?  
✅ **Consistency** – Does the data match across different sources?  
✅ **Validity** – Does the data follow the required format (e.g., date formats, unique constraints)?  
✅ **Integrity** – Are relationships (foreign keys, referential integrity) maintained?  
✅ **Timeliness** – Is data updated as expected in real-time or batch processing?  

---

## **🔹 2. Methods for Data Quality Testing**
### **1️⃣ Schema Validation & Data Type Checks**
Ensures the **data structure** follows the expected schema.

✅ **Example: Validate Data Types & Schema Mismatches**
```sql
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'customers';
```
📌 **Use Case:** Detect **mismatched column types** when migrating from MySQL to SQL Server.

✅ **Python Approach: Pandas for Schema Validation**
```python
import pandas as pd

# Define expected schema
expected_schema = {"customer_id": int, "email": str, "join_date": "datetime64[ns]"}

# Load dataset
df = pd.read_csv("customers.csv")

# Validate data types
for col, dtype in expected_schema.items():
    if df[col].dtype != dtype:
        print(f"Column {col} has incorrect type: {df[col].dtype}, expected {dtype}")
```
📌 **Use Case:** Validates **data types** before inserting data into a database.

---

### **2️⃣ Completeness Testing (Checking for Missing Data)**
Ensures **no important data is missing**.

✅ **Example: Identify Missing Values**
```sql
SELECT * FROM customers WHERE email IS NULL;
```
📌 **Use Case:** Detects **customers with missing email addresses**.

✅ **Python Approach: Check Missing Data in Pandas**
```python
missing_counts = df.isnull().sum()
print(missing_counts[missing_counts > 0])
```
📌 **Use Case:** Detects **columns with missing values** for data cleansing.

---

### **3️⃣ Referential Integrity Testing (Foreign Key Validation)**
Ensures **data relationships are consistent**.

✅ **Example: Find Orders Without a Valid Customer (Orphan Records)**
```sql
SELECT o.order_id 
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```
📌 **Use Case:** Identifies **orders referencing non-existent customers**.

---

### **4️⃣ Duplicate Data Detection**
Ensures **no duplicate records exist**.

✅ **Example: Find Duplicate Customer Records**
```sql
SELECT email, COUNT(*)
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;
```
📌 **Use Case:** Identifies **duplicate email addresses** in customer records.

✅ **Python Approach: Find Duplicate Entries in Pandas**
```python
duplicates = df[df.duplicated(subset=["email"], keep=False)]
print(duplicates)
```
📌 **Use Case:** Finds **duplicate customers based on email**.

---

### **5️⃣ Business Rule Validation**
Ensures **data follows predefined business rules**.

✅ **Example: Validate That Orders Have Positive Amounts**
```sql
SELECT * FROM orders WHERE amount <= 0;
```
📌 **Use Case:** Detects **orders with negative or zero amounts**.

✅ **Python Approach: Check Data Against Business Rules**
```python
invalid_orders = df[df["amount"] <= 0]
print(invalid_orders)
```
📌 **Use Case:** Detects **transactions that violate business rules**.

---

### **6️⃣ Data Consistency Testing Across Sources**
Ensures **data matches across databases, APIs, or systems**.

✅ **Example: Compare Sales Data Between Two Systems**
```sql
SELECT customer_id, SUM(amount) AS total_sales
FROM sales_erp
GROUP BY customer_id
EXCEPT
SELECT customer_id, SUM(amount)
FROM sales_warehouse
GROUP BY customer_id;
```
📌 **Use Case:** Identifies **inconsistencies between ERP and Data Warehouse**.

✅ **Python Approach: Cross-Database Comparison**
```python
df_erp = pd.read_sql("SELECT customer_id, SUM(amount) AS total_sales FROM sales_erp GROUP BY customer_id", conn_erp)
df_dw = pd.read_sql("SELECT customer_id, SUM(amount) AS total_sales FROM sales_warehouse GROUP BY customer_id", conn_dw)

discrepancies = df_erp.merge(df_dw, on="customer_id", suffixes=("_erp", "_dw"))
discrepancies["diff"] = discrepancies["total_sales_erp"] - discrepancies["total_sales_dw"]
print(discrepancies[discrepancies["diff"] != 0])
```
📌 **Use Case:** Detects **mismatched records between ERP and Data Warehouse**.

---

## **🔹 3. Automated Data Validation Tools**
1️⃣ **Great Expectations** – Automates **data validation and testing**.  
2️⃣ **dbt (Data Build Tool)** – Ensures **data integrity in SQL-based data pipelines**.  
3️⃣ **Apache Griffin** – For **big data quality monitoring**.  
4️⃣ **Datafold** – Detects **data discrepancies in ETL workflows**.  

✅ **Example: Using `Great Expectations` for Automated Data Validation**
```python
import great_expectations as ge

df = ge.read_csv("orders.csv")

df.expect_column_values_to_be_between("amount", min_value=1, max_value=10000)
df.expect_column_values_to_not_be_null("customer_id")
```
📌 **Use Case:** Ensures **order amounts are valid and customer IDs are not null**.

---

## **🔹 4. Continuous Monitoring & Alerting**
### **1️⃣ Implement Data Quality Checks in ETL Pipelines**
✅ **Azure Data Factory (ADF) Pipeline Validation**
- Use **Pre-copy script validation** before loading data.  
- Store **failed records in an error logging table**.  

✅ **Example: Logging Data Validation Failures in SQL**
```sql
CREATE TABLE data_quality_log (
    record_id INT PRIMARY KEY,
    error_message VARCHAR(255),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO data_quality_log (record_id, error_message)
SELECT order_id, 'Negative order amount' 
FROM orders 
WHERE amount < 0;
```
📌 **Use Case:** Logs **invalid orders** before inserting them into the database.

---

## **🔹 5. Alerts & Notifications for Data Quality Issues**
### **2️⃣ Set Up Email or Slack Alerts for Failed Validations**
✅ **Example: Python Script for Sending Email Alerts on Data Quality Issues**
```python
import smtplib

def send_alert(subject, message):
    sender = "alerts@example.com"
    recipients = ["data_team@example.com"]
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.sendmail(sender, recipients, f"Subject: {subject}\n\n{message}")

send_alert("Data Quality Issue", "Negative values found in order amounts!")
```
📌 **Use Case:** Sends an **email alert** when data quality validation fails.

---

## **🔹 Final Checklist for Data Quality Testing**
✅ **Schema Validation** – Check **data types, column structures**.  
✅ **Missing Data Detection** – Identify **NULL values and missing records**.  
✅ **Referential Integrity Testing** – Validate **foreign key relationships**.  
✅ **Duplicate Detection** – Remove **redundant records**.  
✅ **Business Rule Validation** – Ensure **data follows expected patterns**.  
✅ **Cross-System Data Consistency** – Compare **data between sources**.  
✅ **Automated Data Quality Tools** – Use **Great Expectations, dbt, Apache Griffin**.  
✅ **ETL Validation Logging & Alerts** – **Log errors and send real-time notifications**.  
