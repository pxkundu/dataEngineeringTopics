### **SQL Basics to Prepare for the SQL Reporting Developer's Interview**

Questions focused on **SQL queries, reporting, data modeling, performance tuning, and optimization**. Below is a **structured SQL preparation guide** covering **all key areas** relevant to this interview.

---

## **🔹 1. SQL Querying Basics**
✅ **SELECT Statement & Filtering Data**
```sql
SELECT first_name, last_name, email 
FROM customers 
WHERE country = 'Germany';
```
✔ **Practice:**
- `SELECT DISTINCT` (removes duplicates).
- `ORDER BY` (sorting results).
- `LIMIT` / `TOP` (restricting results).

---

## **🔹 2. Joins & Relationships**
✅ **Types of Joins (INNER, LEFT, RIGHT, FULL)**
```sql
SELECT customers.first_name, orders.order_id, orders.amount 
FROM customers 
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```
✔ **Know when to use:**  
- **INNER JOIN** → Matches records in both tables.  
- **LEFT JOIN** → Returns all records from the left table + matching records from the right.  
- **RIGHT JOIN** → Opposite of LEFT JOIN.  
- **FULL JOIN** → Returns all records from both tables.

---

## **🔹 3. Aggregate Functions & Grouping**
✅ **SUM, COUNT, AVG, MIN, MAX**
```sql
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 5000;
```
✔ **GROUP BY** → Groups data by a column.  
✔ **HAVING** → Filters grouped data (similar to WHERE but for aggregates).  

---

## **🔹 4. Subqueries & CTEs (Common Table Expressions)**
✅ **Subqueries (Nested Queries)**
```sql
SELECT customer_id, first_name, last_name
FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE amount > 1000);
```
✅ **CTEs for Readability & Reusability**
```sql
WITH CustomerOrders AS (
    SELECT customer_id, SUM(amount) AS total_spent 
    FROM orders 
    GROUP BY customer_id
)
SELECT * FROM CustomerOrders WHERE total_spent > 5000;
```
✔ **CTEs vs. Subqueries** → CTEs are better for **complex queries & reusability**.

---

## **🔹 5. Window Functions (Advanced SQL)**
✅ **ROW_NUMBER(), RANK(), DENSE_RANK()**
```sql
SELECT customer_id, order_id, amount,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rank
FROM orders;
```
✔ **PARTITION BY** → Groups rows before ranking.  
✔ **ORDER BY** → Defines ranking order.  

✅ **Cumulative Sum Example**
```sql
SELECT customer_id, order_date, amount,
       SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS running_total
FROM orders;
```
✔ **Useful for Reporting & Dashboards**.

---

## **🔹 6. SQL Performance Optimization**
✅ **Indexing**
```sql
CREATE INDEX idx_customer_email ON customers(email);
```
✔ **Speeds up searches (`WHERE` and `JOIN` conditions).**  
✔ **Clustered vs. Non-Clustered Indexes**.

✅ **Query Execution Plan**
```sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 1001;
```
✔ Helps identify **slow queries** and **indexing needs**.

---

## **🔹 7. SQL Reporting & Data Visualization**
✅ **Stored Procedures for Reporting**
```sql
CREATE PROCEDURE GetTopCustomers
AS
BEGIN
    SELECT customer_id, SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer_id
    ORDER BY total_spent DESC
    LIMIT 10;
END;
```
✔ Used in **SSRS, Power BI, SAP BOBJ Reports**.

✅ **Dynamic SQL for Reporting**
```sql
DECLARE @Country NVARCHAR(50) = 'USA';

EXEC sp_executesql N'
    SELECT customer_id, first_name, last_name 
    FROM customers WHERE country = @Country', N'@Country NVARCHAR(50)', @Country;
```
✔ **Dynamic queries based on user input**.

---

## **🔹 8. Data Warehousing & Reporting Concepts**
✅ **Star Schema vs. Snowflake Schema**
✔ **Star Schema:** Simple, fewer joins, better for reporting.  
✔ **Snowflake Schema:** More normalized, reduces redundancy.

✅ **ETL Process**
✔ **Extract → Transform → Load** steps for data warehousing.

---

## **🔹 9. Handling Date & Time in SQL**
✅ **Date Functions**
```sql
SELECT GETDATE(); -- Current date & time
SELECT DATEADD(DAY, 7, GETDATE()); -- Adds 7 days
SELECT DATEDIFF(YEAR, '2000-01-01', GETDATE()); -- Difference in years
```
✔ Used for **time-based reporting**.

---

## **🔹 10. Error Handling in SQL**
✅ **Using TRY...CATCH for Error Handling**
```sql
BEGIN TRY
    INSERT INTO customers (customer_id, name, email) VALUES (1, 'John Doe', 'john@example.com');
END TRY
BEGIN CATCH
    PRINT 'Error occurred: ' + ERROR_MESSAGE();
END CATCH;
```
✔ Handles **runtime errors in stored procedures**.

---

### **🔹 Final SQL Interview Preparation Checklist**
✅ **Basic SQL Queries** – `SELECT`, `WHERE`, `GROUP BY`, `HAVING`.  
✅ **Joins & Relationships** – `INNER`, `LEFT`, `RIGHT`, `FULL OUTER JOIN`.  
✅ **Aggregations & Window Functions** – `SUM()`, `AVG()`, `ROW_NUMBER()`.  
✅ **Performance Tuning** – `Indexes`, `Execution Plans`, `CTEs`.  
✅ **SQL for Reporting** – `Stored Procedures`, `SSRS`, `Power BI Integration`.  
✅ **Data Warehousing Concepts** – `Star vs. Snowflake Schema`, `ETL`.  
✅ **Error Handling in SQL** – `TRY...CATCH`, `Logging Errors`.  

---
