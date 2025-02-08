### **Apache Spark Core Technical Commands & Concepts**
Apache Spark provides a robust **distributed computing framework** with various APIs for **batch processing, real-time streaming, machine learning, and graph computation**. Below, you will find an extensive list of essential **Spark commands** covering **RDD, DataFrame, Dataset, Spark SQL, Streaming, and Deployment**.

---

## **1. Spark Initialization Commands**
### **Start Spark Shell (Scala)**
```sh
spark-shell
```
### **Start PySpark Shell**
```sh
pyspark
```
### **Initialize Spark Session in Python**
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkCommands") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
```

---

## **2. RDD (Resilient Distributed Dataset) Commands**
RDD is the **low-level abstraction** of Spark for distributed data processing.

### **Create an RDD**
```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
```

### **RDD Transformations (Lazy Operations)**
| Transformation | Command |
|---------------|---------|
| **Map** | `rdd.map(lambda x: x * 2)` |
| **Filter** | `rdd.filter(lambda x: x % 2 == 0)` |
| **FlatMap** | `rdd.flatMap(lambda x: (x, x*10))` |
| **Distinct** | `rdd.distinct()` |
| **Union** | `rdd1.union(rdd2)` |
| **Intersection** | `rdd1.intersection(rdd2)` |
| **Subtract** | `rdd1.subtract(rdd2)` |
| **Join** | `rdd1.join(rdd2)` |
| **ReduceByKey** | `rdd.reduceByKey(lambda a, b: a + b)` |
| **SortByKey** | `rdd.sortByKey()` |

### **RDD Actions (Triggers Execution)**
| Action | Command |
|--------|---------|
| **Collect** | `rdd.collect()` |
| **Count** | `rdd.count()` |
| **First** | `rdd.first()` |
| **Take** | `rdd.take(3)` |
| **Reduce** | `rdd.reduce(lambda a, b: a + b)` |
| **Save As Text File** | `rdd.saveAsTextFile("output.txt")` |

---

## **3. DataFrame Commands**
DataFrames are **schema-based distributed data structures**.

### **Create DataFrame from List**
```python
data = [("Alice", 30), ("Bob", 25)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
df.show()
```

### **Read and Write Files**
```python
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.write.mode("overwrite").parquet("output.parquet")
```

### **DataFrame Transformations**
| Transformation | Command |
|---------------|---------|
| **Select Columns** | `df.select("Name", "Age")` |
| **Filter Rows** | `df.filter(df["Age"] > 30)` |
| **GroupBy & Aggregate** | `df.groupBy("Age").count()` |
| **Sort Data** | `df.orderBy(df["Age"].desc())` |
| **Add Column** | `df.withColumn("NewCol", df["Age"] * 2)` |
| **Drop Column** | `df.drop("Age")` |
| **Distinct Rows** | `df.distinct()` |

---

## **4. Spark SQL Commands**
SQL-like queries on DataFrames.

### **Register Temporary Table and Run SQL**
```python
df.createOrReplaceTempView("people")
sqlDF = spark.sql("SELECT Name, Age FROM people WHERE Age > 30")
sqlDF.show()
```

### **Using SQL to Aggregate**
```python
spark.sql("SELECT Age, COUNT(*) FROM people GROUP BY Age").show()
```

---

## **5. Dataset Commands (Scala & Java Only)**
Datasets combine **DataFrames' optimizations** with **RDD’s type safety**.

### **Create Dataset in Scala**
```scala
case class Person(name: String, age: Int)
val ds = Seq(Person("Alice", 30), Person("Bob", 25)).toDS()
ds.show()
```

---

## **6. Spark Streaming Commands**
Spark Streaming processes **real-time data**.

### **Read Stream from Kafka**
```python
from pyspark.sql.types import StringType
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic_name") \
    .load()
```

### **Write Stream to Console**
```python
df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start() \
    .awaitTermination()
```

---

## **7. Machine Learning (MLlib) Commands**
Spark MLlib is used for **machine learning**.

### **Load Training Data**
```python
from pyspark.ml.classification import LogisticRegression
training = spark.read.format("libsvm").load("sample_libsvm_data.txt")
```

### **Train a Logistic Regression Model**
```python
lr = LogisticRegression()
model = lr.fit(training)
model.summary.accuracy
```

---

## **8. Spark Performance Optimization Commands**
### **Repartition & Coalesce**
```python
df.repartition(4)  # Increase partitions
df.coalesce(1)  # Reduce partitions
```

### **Enable Adaptive Query Execution (AQE)**
```python
spark.conf.set("spark.sql.adaptive.enabled", "true")
```

### **Cache & Persist Data**
```python
df.cache()
df.persist()
```

---

## **9. Cluster Deployment Commands**
### **Submit a Spark Job**
```sh
spark-submit --master yarn my_script.py
```

### **Check Running Jobs**
```sh
yarn application -list
```

---

## **10. Spark Configuration Commands**
| Setting | Command |
|---------|---------|
| **Set Executor Memory** | `spark.conf.set("spark.executor.memory", "4g")` |
| **Set Cores** | `spark.conf.set("spark.executor.cores", "4")` |
| **Set Parallelism** | `spark.conf.set("spark.sql.shuffle.partitions", "50")` |

---

## **Final Summary**
| Category | Command Example |
|----------|----------------|
| **Initialize Spark** | `spark = SparkSession.builder.getOrCreate()` |
| **RDD Commands** | `rdd.map(lambda x: x*2).collect()` |
| **DataFrame Operations** | `df.select("Name").show()` |
| **Spark SQL** | `spark.sql("SELECT * FROM table")` |
| **Streaming** | `df.writeStream.format("console").start()` |
| **Machine Learning** | `model = lr.fit(training)` |
| **Performance Optimization** | `df.cache()` |
| **Cluster Deployment** | `spark-submit --master yarn script.py` |

