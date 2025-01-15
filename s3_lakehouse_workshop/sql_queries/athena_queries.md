The goal is to set up Athena to query data stored in S3 (processed by the Lambda function) and enable insightful analysis.

---

## **Phase 3: Athena Configuration**

### **Objective**
1. Query processed data stored in S3 using Amazon Athena.
2. Optimize data access by defining a structured schema.
3. Use partitioning to improve query performance.

---

### **Step 1: Organize Processed Data in S3**
1. Processed data should be saved in a **structured format** to make it queryable by Athena.
2. Use partitioning to organize the data by date for efficient querying.

**Expected S3 folder structure:**
```
s3://ecommerce-data-lakehouse/processed/
├── date=2025-01-14/
│   └── processed_data_1679001234.json
├── date=2025-01-15/
│   └── processed_data_1679004567.json
```

3. **File Format**:
   - Athena supports various formats such as **JSON**, **CSV**, **Parquet**, and **ORC**.
   - Parquet is recommended for optimal performance and cost-efficiency.

---

### **Step 2: Create an Athena Database**
Create a database in Athena to organize the tables for querying.

#### **Option 1: Using the AWS Management Console**
1. Go to the **Athena Console**.
2. Click on the **Query editor** tab.
3. Run the following query to create a new database:
   ```sql
   CREATE DATABASE ecommerce_data_lake;
   ```
4. Verify that the database is created:
   ```sql
   SHOW DATABASES;
   ```

#### **Option 2: Using AWS CLI**
```bash
aws athena start-query-execution \
    --query-string "CREATE DATABASE ecommerce_data_lake;" \
    --result-configuration "OutputLocation=s3://ecommerce-data-lakehouse/athena-results/"
```

---

### **Step 3: Define a Table for Processed Data**
Create an external table in Athena that points to the processed data in S3.

#### **SQL to Create the Table:**
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS ecommerce_data_lake.processed_data (
    data_id STRING,
    user_id STRING,
    event_type STRING,
    product STRING,
    timestamp BIGINT,
    processed_at STRING
)
PARTITIONED BY (date STRING)  -- Partitioned by date for query efficiency
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
STORED AS TEXTFILE
LOCATION 's3://ecommerce-data-lakehouse/processed/'
TBLPROPERTIES (
    'skip.header.line.count'='0',
    'serialization.format' = '1'
);
```

#### **Explanation:**
1. **Columns**:
   - `data_id`: Unique identifier for each record.
   - `user_id`: ID of the user who performed the event.
   - `event_type`: Type of event (`view`, `click`, `purchase`).
   - `product`: Product name.
   - `timestamp`: Unix timestamp of the event.
   - `processed_at`: Timestamp of when the data was processed.

2. **Partitioning**:
   - The table is partitioned by `date` to optimize query performance.
   - Data is stored in folders like `date=YYYY-MM-DD/`.

3. **Location**:
   - Points to the `processed/` folder in S3.

4. **Serde and File Format**:
   - Uses **Hive SerDe** to parse JSON or text files.

---

### **Step 4: Add Partitions**
Partitions must be added to Athena when new data is uploaded to the S3 bucket.

#### **Option 1: Using SQL**
Run the following query to add partitions manually:
```sql
ALTER TABLE ecommerce_data_lake.processed_data
ADD PARTITION (date='2025-01-14') LOCATION 's3://ecommerce-data-lakehouse/processed/date=2025-01-14/';
```

#### **Option 2: Automate Partition Updates**
1. Enable AWS Glue integration to automatically update partitions.
2. Use a Lambda function to trigger partition updates when new data is added to S3.

---

### **Step 5: Query the Data**
Run queries to analyze the processed data.

#### **1. Count Events by Product**
```sql
SELECT product, COUNT(*) AS total_events
FROM ecommerce_data_lake.processed_data
WHERE date = '2025-01-14'
GROUP BY product;
```

#### **2. User Engagement**
```sql
SELECT user_id, COUNT(*) AS total_interactions
FROM ecommerce_data_lake.processed_data
WHERE date = '2025-01-14'
GROUP BY user_id
ORDER BY total_interactions DESC;
```

#### **3. Events Over Time**
```sql
SELECT date, event_type, COUNT(*) AS event_count
FROM ecommerce_data_lake.processed_data
GROUP BY date, event_type
ORDER BY date ASC, event_type ASC;
```

---

### **Step 6: Verify Athena Query Results**
1. Query results are stored in the specified S3 location.
2. By default, results are saved in:
   ```
   s3://<your-query-results-bucket>/Unsaved/
   ```

---

### **Step 7: Automate Query Result Cleanup**
Use an S3 lifecycle policy to automatically delete query results after a specified period (e.g., 30 days).

#### **CDK Code for Lifecycle Policy**
Add the following lifecycle policy to the S3 bucket in the `AthenaStack`:
```python
self.s3_bucket.add_lifecycle_rule(
    id="QueryResultsCleanup",
    prefix="athena-results/",
    expiration=Duration.days(30)
)
```

---

### **Testing Athena**
1. Upload processed data to the `processed/` folder in S3.
2. Add partitions using SQL or automation.
3. Run example queries to verify the setup.

---