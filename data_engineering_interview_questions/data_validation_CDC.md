### **Change Data Capture (CDC) and Its Applications**  

## **🔹 1. What is Change Data Capture (CDC)?**
CDC is a technique used to **track and capture changes (INSERT, UPDATE, DELETE) in a database** so that downstream systems can react to those changes in **real-time** or **batch mode**.

✅ **Key Use Cases of CDC:**  
✔ **Real-time ETL Pipelines** – Stream **only modified data** instead of full table refresh.  
✔ **Database Replication** – Sync **on-prem databases to cloud (e.g., SQL Server to Azure Synapse, MySQL to BigQuery).**  
✔ **Event-Driven Architectures** – Publish **CDC events to Kafka for streaming applications.**  
✔ **Data Warehousing** – Improve **data freshness by only updating changed records.**  

---

## **🔹 2. CDC Techniques & Implementations**
CDC can be implemented in **different ways**, depending on the database system.

### **1️⃣ Transaction Log-Based CDC (Best for Real-time Streaming)**
✔ **How it Works:**  
- Reads **database transaction logs** (`binlog`, `redo log`, `write-ahead log`).
- Identifies **INSERT, UPDATE, DELETE events**.
- Sends **only modified data** to consumers.

✅ **Example: SQL Server CDC Using Transaction Log**  
```sql
-- Enable CDC on a database
EXEC sys.sp_cdc_enable_db;

-- Enable CDC on a table
EXEC sys.sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = 'customers',
    @role_name = NULL;
```
📌 **Use Case:** **Efficient replication and real-time event processing in Azure Synapse or Kafka.**  

✅ **Pros:**  
✔ **Minimal impact on source database**.  
✔ **Best for high-velocity transactional systems**.  
✔ Works well with **Kafka, Debezium, and streaming frameworks (Spark, Flink, AWS DMS).**  

❌ **Cons:**  
- Requires **access to transaction logs** (may not be possible in managed databases).  
- **Storage overhead** for logs if not cleaned properly.  

---

### **2️⃣ Trigger-Based CDC (Best for Small Databases & Simplicity)**
✔ **How it Works:**  
- Uses **SQL triggers** to capture changes and store them in a tracking table.  
- Example: When an **INSERT/UPDATE/DELETE occurs**, a **trigger logs the change**.

✅ **Example: MySQL CDC Using Triggers**  
```sql
CREATE TABLE customer_changes (
    change_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    change_type ENUM('INSERT', 'UPDATE', 'DELETE'),
    change_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER after_customer_update
AFTER UPDATE ON customers
FOR EACH ROW
INSERT INTO customer_changes (customer_id, change_type) 
VALUES (OLD.customer_id, 'UPDATE');
```
📌 **Use Case:** **Simple audit logging and tracking changes in small databases.**  

✅ **Pros:**  
✔ **Easy to implement** without requiring transaction log access.  
✔ **Good for auditing and compliance.**  

❌ **Cons:**  
- **Performance overhead** on high-traffic tables.  
- **Not scalable** for big data pipelines.  

---

### **3️⃣ Timestamp-Based CDC (Best for Batch ETL Updates)**
✔ **How it Works:**  
- Relies on a **last_modified column** in tables.  
- Extracts **only records that changed since the last ETL run**.

✅ **Example: Incremental Load Using Timestamps**  
```sql
SELECT * FROM orders
WHERE last_modified >= DATE_SUB(NOW(), INTERVAL 1 DAY);
```
📌 **Use Case:** **Updating Data Warehouses (e.g., Azure Synapse, Snowflake, BigQuery).**  

✅ **Pros:**  
✔ **Low database impact** (does not require logs or triggers).  
✔ **Simple and easy to implement**.  

❌ **Cons:**  
- **Deletes cannot be detected** unless soft deletes are used.  
- **Requires application-level updates to maintain `last_modified` column.**  

---

## **🔹 3. CDC in Cloud & Big Data Architectures**
CDC is widely used in **modern cloud data platforms** for **real-time analytics and event-driven architectures**.

### **1️⃣ AWS Database Migration Service (DMS)**
✅ **Use Case:** **Replicating on-prem SQL Server changes to Amazon Redshift in real-time.**  
✅ **How?**  
- AWS DMS enables **log-based CDC** from **Oracle, SQL Server, PostgreSQL, and MySQL**.  
- Streams changes into **Redshift, S3, or Kinesis**.

---

### **2️⃣ Apache Kafka & Debezium for Streaming CDC**
✅ **Use Case:** **Streaming MySQL changes to Kafka and Spark.**  
✅ **How?**  
- Debezium captures **transaction logs from MySQL, PostgreSQL, SQL Server, and MongoDB**.  
- Publishes changes to **Kafka topics for real-time processing.**  

💡 **Example: Streaming MySQL Changes to Kafka**
```json
{
  "name": "mysql-connector",
  "config": {
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "database.hostname": "mysql-server",
    "database.port": "3306",
    "database.user": "debezium",
    "database.password": "password",
    "database.server.id": "1",
    "database.include.list": "inventory",
    "table.include.list": "inventory.customers",
    "topic.prefix": "dbz",
    "snapshot.mode": "initial"
  }
}
```
📌 **When to use?**  
✔ **Streaming ETL (ELT) Pipelines**.  
✔ **Microservices & Event-Driven Applications**.  
✔ **Processing database changes in real-time with Kafka & Spark.**  

---

### **3️⃣ Google BigQuery & Snowflake CDC**
✅ **Use Case:** **CDC for analytics pipelines in GCP & Snowflake.**  
✅ **How?**  
- Use **Cloud Data Fusion (GCP) or Snowflake Streams** to capture **incremental data changes**.  

---

## **🔹 4. When to Use CDC vs. Full Table Refresh**
| **Use Case** | **CDC (Change Data Capture)** | **Full Table Refresh** |
|-------------|---------------------|---------------------|
| **Real-time Updates** | ✅ Yes | ❌ No |
| **Minimize Database Load** | ✅ Yes | ❌ No |
| **Works with Streaming (Kafka, Spark)** | ✅ Yes | ❌ No |
| **Works for Historical Snapshots** | ❌ No | ✅ Yes |
| **Easy Implementation** | ❌ No (Needs setup) | ✅ Yes (Simple query) |

📌 **CDC is best when minimizing load, ensuring real-time updates, and integrating with event-driven architectures.**  

---