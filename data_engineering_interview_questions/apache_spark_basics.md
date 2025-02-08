Here are some **basic Apache Spark commands** to get started with **PySpark**.

---

### **1. Starting a Spark Session**
Before running any Spark commands, you need to start a **SparkSession**.

```python
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("BasicSparkCommands").getOrCreate()
```

---

### **2. Creating a DataFrame**
Create a **DataFrame** from a list of tuples.

```python
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)
df.show()
```
**Output:**
```
+-------+---+
|   Name|Age|
+-------+---+
|  Alice| 30|
|    Bob| 25|
|Charlie| 35|
+-------+---+
```

---

### **3. Reading a CSV File**
Load a CSV file into a **Spark DataFrame**.

```python
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
df.show()
df.printSchema()
```

---

### **4. Basic DataFrame Operations**
#### **Select Columns**
```python
df.select("Name").show()
```
#### **Filter Rows**
```python
df_filtered = df.filter(df["Age"] > 30)
df_filtered.show()
```
#### **Sorting**
```python
df_sorted = df.orderBy(df["Age"].desc())
df_sorted.show()
```
#### **Group By and Aggregate**
```python
df.groupBy("Age").count().show()
```

---

### **5. Writing Data to a File**
Save a **DataFrame** to different formats.

#### **Write Data to CSV**
```python
df.write.mode("overwrite").csv("output.csv", header=True)
```

#### **Write Data to Parquet**
```python
df.write.mode("overwrite").parquet("output.parquet")
```

---

### **6. Creating an RDD**
RDD (Resilient Distributed Dataset) is Spark’s low-level abstraction.

```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
print(rdd.collect())  # Output: [1, 2, 3, 4, 5]
```

---

### **7. Running SQL Queries on DataFrames**
Convert a DataFrame into a **temporary SQL table** and run SQL queries.

```python
df.createOrReplaceTempView("people")

sql_df = spark.sql("SELECT Name, Age FROM people WHERE Age > 30")
sql_df.show()
```

---

### **8. Repartitioning and Coalescing**
To optimize performance by managing partitions.

```python
df = df.repartition(4)  # Increase partitions to 4
df = df.coalesce(1)      # Reduce partitions to 1
```

---

### **9. Checking Number of Partitions**
```python
print(df.rdd.getNumPartitions())
```

---

### **10. Stopping Spark Session**
Once done, **stop the Spark session**.

```python
spark.stop()
```

---
