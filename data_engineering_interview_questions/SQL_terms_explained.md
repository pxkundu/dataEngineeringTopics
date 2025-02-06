### **🚀 Comprehensive Guide to SQL Terms (Basic → Advanced) with Explanations & Examples**
This guide covers SQL **from fundamentals to advanced concepts** with clear explanations and practical examples.

---

## **🔹 1. SQL Basics**
### **1️⃣ SELECT Statement**
✅ **Used to retrieve data from a table**.  
```sql
SELECT first_name, last_name FROM customers;
```
📌 **Example:** Retrieves all first and last names from the `customers` table.

---

### **2️⃣ WHERE Clause**
✅ **Filters data based on a condition**.  
```sql
SELECT * FROM orders WHERE amount > 500;
```
📌 **Example:** Retrieves all orders where the amount is greater than **500**.

---

### **3️⃣ ORDER BY Clause**
✅ **Sorts the result set in ascending (`ASC`) or descending (`DESC`) order.**  
```sql
SELECT * FROM customers ORDER BY last_name ASC;
```
📌 **Example:** Retrieves all customers sorted by **last name in ascending order**.

---

### **4️⃣ DISTINCT Keyword**
✅ **Removes duplicate values in the result set.**  
```sql
SELECT DISTINCT country FROM customers;
```
📌 **Example:** Retrieves **unique country names** from the `customers` table.

---

### **5️⃣ LIMIT / TOP Clause**
✅ **Restricts the number of records returned.**  
```sql
SELECT * FROM orders ORDER BY amount DESC LIMIT 5;
```
📌 **Example:** Retrieves **top 5 highest orders**.

---

## **🔹 2. SQL Joins**
### **6️⃣ INNER JOIN**
✅ **Retrieves matching records from both tables.**  
```sql
SELECT customers.first_name, orders.order_id 
FROM customers 
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```
📌 **Example:** Retrieves **only customers who have placed orders**.

---

### **7️⃣ LEFT JOIN**
✅ **Returns all records from the left table, even if there’s no match in the right table.**  
```sql
SELECT customers.first_name, orders.order_id 
FROM customers 
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
```
📌 **Example:** Retrieves **all customers, even those without orders**.

---

### **8️⃣ RIGHT JOIN**
✅ **Returns all records from the right table, even if there’s no match in the left table.**  
```sql
SELECT customers.first_name, orders.order_id 
FROM customers 
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
```
📌 **Example:** Retrieves **all orders, even those that don’t have a customer**.

---

### **9️⃣ FULL JOIN**
✅ **Returns all records when there is a match in either table.**  
```sql
SELECT customers.first_name, orders.order_id 
FROM customers 
FULL JOIN orders ON customers.customer_id = orders.customer_id;
```
📌 **Example:** Retrieves **all customers and all orders, matching where possible**.

---

## **🔹 3. SQL Aggregations & Grouping**
### **🔟 COUNT, SUM, AVG, MIN, MAX**
✅ **Aggregate functions perform calculations on data.**
```sql
SELECT COUNT(order_id) AS total_orders FROM orders;
SELECT SUM(amount) AS total_sales FROM orders;
SELECT AVG(amount) AS avg_sales FROM orders;
SELECT MIN(amount) AS min_sale FROM orders;
SELECT MAX(amount) AS max_sale FROM orders;
```
📌 **Example:** Retrieves **total orders, total sales, average order amount, and min/max sales**.

---

### **1️⃣1️⃣ GROUP BY Clause**
✅ **Used to group records by a specific column.**  
```sql
SELECT country, COUNT(customer_id) AS total_customers
FROM customers
GROUP BY country;
```
📌 **Example:** Retrieves the **total number of customers per country**.

---

### **1️⃣2️⃣ HAVING Clause**
✅ **Filters grouped records (like WHERE, but for aggregates).**  
```sql
SELECT country, COUNT(customer_id) AS total_customers
FROM customers
GROUP BY country
HAVING COUNT(customer_id) > 50;
```
📌 **Example:** Retrieves **only countries with more than 50 customers**.

---

## **🔹 4. SQL Subqueries & CTEs**
### **1️⃣3️⃣ Subquery (Nested Query)**
✅ **A query inside another query.**  
```sql
SELECT first_name, last_name 
FROM customers
WHERE customer_id IN (
    SELECT customer_id FROM orders WHERE amount > 1000
);
```
📌 **Example:** Retrieves **customers who have placed orders above $1000**.

---

### **1️⃣4️⃣ Common Table Expressions (CTEs)**
✅ **A temporary result set used to improve query readability.**  
```sql
WITH CustomerOrders AS (
    SELECT customer_id, SUM(amount) AS total_spent 
    FROM orders 
    GROUP BY customer_id
)
SELECT * FROM CustomerOrders WHERE total_spent > 5000;
```
📌 **Example:** Retrieves **customers who have spent more than $5000**.

---

## **🔹 5. SQL Window Functions**
### **1️⃣5️⃣ ROW_NUMBER()**
✅ **Assigns a unique row number within a partition.**  
```sql
SELECT customer_id, amount, 
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rank
FROM orders;
```
📌 **Example:** Ranks **each order per customer**.

---

### **1️⃣6️⃣ RANK() and DENSE_RANK()**
✅ **Ranks records with handling for ties.**  
```sql
SELECT customer_id, amount, 
       RANK() OVER (ORDER BY amount DESC) AS rank
FROM orders;
```
📌 **Example:** Ranks **orders by amount, skipping ranks for ties**.

---

### **1️⃣7️⃣ LEAD() and LAG()**
✅ **Compares current row with previous/next row.**  
```sql
SELECT customer_id, amount, 
       LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_amount
FROM orders;
```
📌 **Example:** Retrieves **previous order amount for each customer**.

---

## **🔹 6. SQL Performance Optimization**
### **1️⃣8️⃣ Indexing**
✅ **Speeds up data retrieval using indexes.**  
```sql
CREATE INDEX idx_customer_email ON customers(email);
```
📌 **Example:** Creates an **index on `email` column** to speed up searches.

---

### **1️⃣9️⃣ Query Execution Plan**
✅ **Analyzes query performance.**  
```sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 1001;
```
📌 **Example:** Shows **how the query executes and where optimizations can be made**.

---

## **🔹 7. SQL Error Handling & Transactions**
### **2️⃣0️⃣ Handling Errors with TRY...CATCH**
✅ **Prevents query failures.**  
```sql
BEGIN TRY
    INSERT INTO customers (customer_id, name, email) VALUES (1, 'John Doe', 'john@example.com');
END TRY
BEGIN CATCH
    PRINT 'Error: ' + ERROR_MESSAGE();
END CATCH;
```
📌 **Example:** Catches **SQL errors during inserts**.

---

### **2️⃣1️⃣ Transactions (COMMIT & ROLLBACK)**
✅ **Ensures atomicity in multi-step operations.**  
```sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

COMMIT;
```
📌 **Example:** Transfers **money between accounts safely**.

---

## **🚀 Final Thoughts**
### **📌 SQL Learning Path:**
✅ **Master Basic Queries** → `SELECT`, `WHERE`, `ORDER BY`  
✅ **Learn Joins & Aggregations** → `INNER JOIN`, `GROUP BY`, `HAVING`  
✅ **Understand Advanced SQL** → `CTEs`, `Window Functions`, `Indexing`  
✅ **Optimize & Secure Queries** → `Indexes`, `Transactions`, `Error Handling`  

