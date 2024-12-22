### **Real-World Project: Building a Big Data Pipeline**

#### **Project Use Case**
**"E-Commerce Analytics Pipeline"**: 
- The project will collect user activity logs (clicks, searches) from an e-commerce website, store the data in Hadoop, and process it using MapReduce, Hive, and Sqoop to generate insights like:
  - The most searched product.
  - User activity trends.

---

### **Project Structure**
We will organize the project folder as follows:

```
ecommerce-analytics/
│
├── logs/                     # Raw activity logs
├── data/                     # HDFS staging area
├── mapper.py                 # MapReduce mapper script
├── reducer.py                # MapReduce reducer script
├── flume/                    # Flume configuration files
│   └── flume.conf
├── hive/                     # Hive scripts
│   ├── create_table.hql
│   └── analytics_queries.hql
├── sqoop/                    # Sqoop commands
│   ├── sqoop_import.sh
│   └── sqoop_export.sh
└── README.md                 # Documentation
```

---

### **Step 1: Generate and Ingest Logs**

1. **Simulate E-Commerce Logs:**
   Generate a sample log file (`logs/activity.log`):
   ```bash
   mkdir -p logs
   echo "timestamp,userid,action,product\n" > logs/activity.log
   echo "2024-12-01T12:00:00,101,search,laptop" >> logs/activity.log
   echo "2024-12-01T12:05:00,102,click,smartphone" >> logs/activity.log
   echo "2024-12-01T12:10:00,101,search,smartphone" >> logs/activity.log
   ```

2. **Ingest Logs with Flume:**
   Create `flume/flume.conf`:
   ```properties
   agent1.sources = source1
   agent1.sinks = sink1
   agent1.channels = channel1

   agent1.sources.source1.type = exec
   agent1.sources.source1.command = tail -f logs/activity.log

   agent1.sinks.sink1.type = hdfs
   agent1.sinks.sink1.hdfs.path = hdfs://localhost:9000/user/ecommerce/logs

   agent1.channels.channel1.type = memory
   agent1.sources.source1.channels = channel1
   agent1.sinks.sink1.channel = channel1
   ```

   Start Flume:
   ```bash
   flume-ng agent --conf flume/ --name agent1 -Dflume.root.logger=INFO,console
   ```

---

### **Step 2: Process Logs Using MapReduce**

1. **MapReduce Scripts:**
   - `mapper.py`:
     ```python
     #!/usr/bin/env python3
     import sys
     for line in sys.stdin:
         data = line.strip().split(",")
         if len(data) == 4 and data[2] == "search":
             print(f"{data[3]}\t1")  # Emit product and count
     ```

   - `reducer.py`:
     ```python
     #!/usr/bin/env python3
     import sys
     from collections import defaultdict

     product_counts = defaultdict(int)
     for line in sys.stdin:
         product, count = line.strip().split("\t")
         product_counts[product] += int(count)

     for product, count in product_counts.items():
         print(f"{product}\t{count}")
     ```

2. **Run MapReduce Job:**
   ```bash
   hadoop jar /path/to/hadoop-streaming.jar \
     -input /user/ecommerce/logs \
     -output /user/ecommerce/output \
     -mapper mapper.py \
     -reducer reducer.py
   ```

3. **View Results:**
   ```bash
   hdfs dfs -cat /user/ecommerce/output/part-00000
   ```

---

### **Step 3: Analyze Data Using Hive**

1. **Create Hive Table:**
   Create `hive/create_table.hql`:
   ```sql
   CREATE EXTERNAL TABLE IF NOT EXISTS ecommerce_logs (
       timestamp STRING,
       userid STRING,
       action STRING,
       product STRING
   )
   ROW FORMAT DELIMITED
   FIELDS TERMINATED BY ','
   STORED AS TEXTFILE
   LOCATION '/user/ecommerce/logs';
   ```

   Execute:
   ```bash
   hive -f hive/create_table.hql
   ```

2. **Run Analytics Queries:**
   Create `hive/analytics_queries.hql`:
   ```sql
   SELECT product, COUNT(*) AS search_count
   FROM ecommerce_logs
   WHERE action = 'search'
   GROUP BY product
   ORDER BY search_count DESC;
   ```

   Execute:
   ```bash
   hive -f hive/analytics_queries.hql
   ```

---

### **Step 4: Export Data to MySQL with Sqoop**

1. **Set Up MySQL Table:**
   ```sql
   CREATE DATABASE ecommerce;
   USE ecommerce;
   CREATE TABLE product_search_counts (
       product VARCHAR(255),
       search_count INT
   );
   ```

2. **Export Hive Data to MySQL:**
   Create `sqoop/sqoop_export.sh`:
   ```bash
   sqoop export \
     --connect jdbc:mysql://localhost/ecommerce \
     --username root --password password \
     --table product_search_counts \
     --export-dir /user/ecommerce/output \
     --fields-terminated-by '\\t'
   ```

   Execute:
   ```bash
   sh sqoop/sqoop_export.sh
   ```

---

### **Step 5: Tips and Tricks**

1. **Log Monitoring:** Use `tail` and `hdfs dfs -tail` to debug ingestion pipelines.
2. **Optimize MapReduce:**
   - Use a Combiner for local aggregation in the Mapper phase.
   - Partition data for better reducer balancing.
3. **Hive Optimization:**
   - Partition tables by date for faster queries.
   - Use ORC file format for better compression and query performance.
4. **Automate Pipelines:** Use Airflow or Oozie to schedule Flume, MapReduce, and Sqoop jobs.

---

### **Step 6: Documentation**

Include a `README.md` file explaining:
- Project purpose.
- Step-by-step setup.
- How to run each component.

---

Would you like a detailed `README.md` template or more elaboration on any component? Let me know! 🚀