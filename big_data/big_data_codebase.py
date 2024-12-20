import sys
from collections import defaultdict

# big_data_codebase.py

# Module 2: Big Data with Hadoop

# Introduction and Install Hadoop
# Hadoop is an open-source framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models.

# HDFS: What it is, and how it works
# HDFS (Hadoop Distributed File System) is the primary storage system used by Hadoop applications. It provides high-throughput access to application data and is suitable for applications that have large data sets.

# Installing Dataset into HDFS
# To install a dataset into HDFS, you need to use the Hadoop command line interface (CLI).

# HDFS Architecture Read/Write Anatomy
# HDFS follows a master-slave architecture where the master node is called NameNode and the slave nodes are called DataNodes.

# HDFS commands
# Example HDFS commands:
# - hdfs dfs -mkdir /user/hadoop/input
# - hdfs dfs -put localfile.txt /user/hadoop/input
# - hdfs dfs -ls /user/hadoop/input
# - hdfs dfs -cat /user/hadoop/input/localfile.txt

# YARN explained
# YARN (Yet Another Resource Negotiator) is the resource management layer of Hadoop. It allows multiple data processing engines such as batch processing, stream processing, interactive processing, and real-time processing to run and process data stored in HDFS.

# Classical version of MapReduce
# MapReduce is a programming model for processing large data sets with a distributed algorithm on a cluster.

# MapReduce: What it is, and how it works
# MapReduce works by breaking the processing into two phases: the Map phase and the Reduce phase.

# MapReduce Architecture: Word Count Program
# Example of a simple MapReduce word count program in Python using Hadoop Streaming:


# Mapper function
def mapper():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print(f"{word}\t1")

# Reducer function
def reducer():
    current_word = None
    current_count = 0
    word = None

    for line in sys.stdin:
        word, count = line.strip().split('\t', 1)
        try:
            count = int(count)
        except ValueError:
            continue

        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(f"{current_word}\t{current_count}")
            current_word = word
            current_count = count

    if current_word == word:
        print(f"{current_word}\t{current_count}")

# MapReduce Combiner & Partitioner concepts and practical demo
# Combiners are mini-reducers that process the output of the map phase to reduce the amount of data transferred to the reducers.
# Partitioners determine how the map output is distributed among the reducers.

# MapReduce Distributed Cache
# The Distributed Cache is a facility provided by the MapReduce framework to cache files needed by applications.

# MapSideJoin and ReduceSideJoin
# Map-side join is a join operation performed at the map phase, while reduce-side join is performed at the reduce phase.

# Integrating DBMS with Hadoop
# Setting up MySQL Server and creating & loading datasets into MySQL
# Example commands to set up MySQL and load data:
# - sudo apt-get install mysql-server
# - mysql -u root -p
# - CREATE DATABASE mydatabase;
# - USE mydatabase;
# - CREATE TABLE mytable (id INT, name VARCHAR(100));
# - LOAD DATA LOCAL INFILE 'data.csv' INTO TABLE mytable FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

# Sqoop Architecture
# Sqoop is a tool designed to transfer data between Hadoop and relational databases.

# Writing the Sqoop Import Commands to transfer data from RDBMS to HDFS/Hive
# Example Sqoop import command:
# - sqoop import --connect jdbc:mysql://localhost/mydatabase --username root --password mypassword --table mytable --target-dir /user/hadoop/mytable

# Writing the Sqoop Export Commands to transfer data from HDFS/Hive to RDBMS
# Example Sqoop export command:
# - sqoop export --connect jdbc:mysql://localhost/mydatabase --username root --password mypassword --table mytable --export-dir /user/hadoop/mytable

# Flume explained
# Flume is a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data.

# Set up Flume and publish logs with it
# Example Flume configuration to publish logs:
# - agent.sources = source1
# - agent.sinks = sink1
# - agent.channels = channel1
# - agent.sources.source1.type = exec
# - agent.sources.source1.command = tail -F /var/log/syslog
# - agent.sinks.sink1.type = hdfs
# - agent.sinks.sink1.hdfs.path = hdfs://localhost:9000/user/hadoop/logs
# - agent.channels.channel1.type = memory
# - agent.sources.source1.channels = channel1
# - agent.sinks.sink1.channel = channel1

# Set up Flume to monitor a directory and store its data in HDFS
# Example Flume configuration to monitor a directory:
# - agent.sources = source1
# - agent.sinks = sink1
# - agent.channels = channel1
# - agent.sources.source1.type = spooldir
# - agent.sources.source1.spoolDir = /var/log/flume
# - agent.sinks.sink1.type = hdfs
# - agent.sinks.sink1.hdfs.path = hdfs://localhost:9000/user/hadoop/flume
# - agent.channels.channel1.type = memory
# - agent.sources.source1.channels = channel1
# - agent.sinks.sink1.channel = channel1

# Use case implementation in Flume
# Example use case: Collecting web server logs and storing them in HDFS for analysis.

# Hive: Use Hive to find the most popular game
# Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis.

# How Hive works
# Hive translates SQL-like queries into MapReduce jobs for execution.

# Hive Architecture
# Hive consists of three main components: HiveQL, Hive Metastore, and Hive Execution Engine.

# Hive Metastore
# The Hive Metastore stores metadata about tables, columns, partitions, and the data types stored in the Hive warehouse.

# Hive Partitioning and Bucketing
# Partitioning divides a table into related parts based on the values of partition columns.
# Bucketing divides data into a fixed number of buckets to optimize query performance.

# Hive file Format
# Hive supports various file formats such as Text, SequenceFile, RCFile, ORC, and Parquet.

# Hive JSON, CSV, XML, ORC & Regex Serde
# SerDe (Serializer/Deserializer) is used to read and write data in Hive tables.

# Use Hive to find the game with the highest average rating
# Example Hive query:
# - CREATE TABLE games (game_id INT, game_name STRING, rating FLOAT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;
# - LOAD DATA INPATH '/user/hadoop/games.csv' INTO TABLE games;
# - SELECT game_name, AVG(rating) as avg_rating FROM games GROUP BY game_name ORDER BY avg_rating DESC LIMIT 1;

# Skills Evaluation
# Practice and hands-on experience with the above concepts and tools will help in mastering big data technologies.

# Module 3: Spark and PySpark
# Spark is a unified analytics engine for large-scale data processing.
# PySpark is the Python API for Spark.
# Spark Core: Provides the core functionality of Spark, including data structures and execution engine.
# Spark SQL: Provides support for structured data processing, including SQL and DataFrames.
# Spark Streaming: Provides support for real-time data processing.
# Spark MLlib: Provides support for machine learning algorithms.
# Spark GraphX: Provides support for graph processing.
# Spark Core Concepts: RDDs, Transformations, Actions, and Partitions.
# Spark DataFrames: A high-level API for structured data processing.
# Spark Datasets: A high-level API for structured data processing with type safety.
# Spark SQL: A high-level API for structured data processing with SQL support.
# Spark MLlib: A high-level API for machine learning algorithms.
# Spark GraphX: A high-level API for graph processing.
# Use Spark to find the top 10 games with the highest average rating
# Example Spark code:
# - data = sc.textFile("/user/hadoop/games.csv")
# - data = data.map(lambda x: x.split(","))
# - df = data.toDF(["game_id", "game_name", "rating"])
# - df.createOrReplaceTempView("games")
# - spark.sql("SELECT game_name, AVG(rating) as avg_rating FROM games GROUP BY
# game_name ORDER BY avg_rating DESC LIMIT 10").show()
# Spark Streaming: Process real-time data using Spark Streaming.
# Example Spark Streaming code:
# - from pyspark.streaming import StreamingContext
# - from pyspark.streaming.kafka import KafkaUtils
# - ssc = StreamingContext(sc, 1)
# - kafka_stream = KafkaUtils.createDirectStream(ssc, ["games"], {"metadata.broker.list": "localhost:9092"})
# - kafka_stream.map(lambda x: x[1]).map(lambda x: x.split(",")).pprint()
# Spark MLlib: Use machine learning algorithms with Spark MLlib.
# Example Spark MLlib code:
# - from pyspark.ml.regression import LinearRegression
# - from pyspark.ml.feature import VectorAssembler
# - data = spark.read.csv("/user/hadoop/data.csv", header=True, inferSchema=True)
# - assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
# - df = assembler.transform(data)
# - lr = LinearRegression(featuresCol="features", labelCol="label")
# - model = lr.fit(df)
# - predictions = model.transform(df)
# Spark GraphX: Use graph processing with Spark GraphX.
# Example Spark GraphX code:
# - from graphframes import GraphFrame
# - vertices = spark.read.csv("/user/hadoop/vertices.csv", header=True, inferSchema=True)
# - edges = spark.read.csv("/user/hadoop/edges.csv", header=True, inferSchema=True)
# - g = GraphFrame(vertices, edges)
# - g.vertices.show()
# - g.edges.show()
# - g = g.filter(g.vertices["age"] > 18)
# - g.vertices.show()
# - g.edges.show()
# - g = g.filter(g.edges["weight"] > 5)
# - g.vertices.show()
# - g.edges.show()
# Skills Evaluation
# 1. Data Analysis: Evaluate the ability to analyze data using Spark.
# 2. Data Processing: Evaluate the ability to process data using Spark.
# 3. Machine Learning: Evaluate the ability to apply machine learning algorithms using Spark MLlib.
# 4. Graph Processing: Evaluate the ability to process graphs using Spark GraphX.
# 5. SQL: Evaluate the ability to use Spark SQL for structured data processing.
# Module 4: Kafka and Real-Time Data Processing
# Kafka: A distributed streaming platform for high-throughput and fault-tolerant data processing.
# Kafka Streams: A Java library for building real-time data processing applications.
# Kafka Connect: A framework for connecting Kafka with external systems.
# Kafka Producer: A producer for sending messages to Kafka topics.
# Kafka Consumer: A consumer for reading messages from Kafka topics.
# Kafka Streams Example: Create a Kafka Streams application to process real-time data.
# Example Kafka Streams code:
# - KStream<String, String> stream = builder.stream("input-topic");
# - stream.mapValues(value -> value.toUpperCase()).to("output-topic");
# Kafka Connect Example: Create a Kafka Connect application to connect Kafka with an external system.
# Example Kafka Connect code:
# - Properties props = new Properties();
# - props.put("bootstrap.servers", "localhost:9092");
# - props.put("key.deserializer", StringDeserializer.class);
# - props.put("value.deserializer", StringDeserializer.class);
# - KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
# - consumer.subscribe(Collections.singletonList("input-topic"));
# - while (true) {
# -   ConsumerRecords<String, String> records = consumer.poll(100);
# -   for (ConsumerRecord<String, String> record : records) {
# -     System.out.println(record.value());
# -   }
# - }
# Kafka Producer Example: Create a Kafka Producer application to send messages to Kafka topics.
# Example Kafka Producer code:
# - Properties props = new Properties();
# - props.put("bootstrap.servers", "localhost:9092");
# - props.put("key.serializer", StringSerializer.class);
# - props.put("value.serializer", StringSerializer.class);
# - KafkaProducer<String, String> producer = new KafkaProducer<>(props);
# - ProducerRecord<String, String> record = new ProducerRecord<>("input-topic", "key", "value");
# - producer.send(record);
# Kafka Consumer Example: Create a Kafka Consumer application to read messages from Kafka topics.
# Example Kafka Consumer code:
# - Properties props = new Properties();
# - props.put("bootstrap.servers", "localhost:9092");
# - props.put("key.deserializer", StringDeserializer.class);
# - props.put("value.deserializer", StringDeserializer.class);
# - KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
# - consumer.subscribe(Collections.singletonList("output-topic"));
# - while (true) {
# -   ConsumerRecords<String, String> records = consumer.poll(100);
# -   for (ConsumerRecord<String, String> record : records) {
# -     System.out.println(record.value());
# -   }
# - }
# Kafka Streams Example: Create a Kafka Streams application to process real-time data.
# Example Kafka Streams code:
# - KStream<String, String> stream = builder.stream("input-topic");
# - stream.mapValues(value -> value.toUpperCase()).to("output-topic");
# Kafka Connect Example: Create a Kafka Connect application to connect Kafka with an external system.
# Example Kafka Connect code:
# - Properties props = new Properties();
# - props.put("bootstrap.servers", "localhost:9092");
# - props.put("key.deserializer", StringDeserializer.class);
# - props.put("value.deserializer", StringDeserializer.class);
# - KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
# - consumer.subscribe(Collections.singletonList("input-topic"));
# - while (true) {
# -   ConsumerRecords<String, String> records = consumer.poll(100);
# -   for (ConsumerRecord<String, String> record : records) {
# -     System.out.println(record.value());
# -   }
# - }
# Kafka Producer Example: Create a Kafka Producer application to send messages to Kafka topics.
# Example Kafka Producer code:
# - Properties props = new Properties();
# - props.put("bootstrap.servers", "localhost:9092");
# - props.put("key.serializer", StringSerializer.class);
# - props.put("value.serializer", StringSerializer.class);
# - KafkaProducer<String, String> producer = new KafkaProducer<>(props);
# - ProducerRecord<String, String> record = new ProducerRecord<>("input-topic", "key",
# - "value");
# - producer.send(record);
# Kafka Consumer Example: Create a Kafka Consumer application to read messages from Kafka topics.
# Example Kafka Consumer code:
# - Properties props = new Properties();
# - props.put("bootstrap.servers", "localhost:9092");
# - props.put("key.deserializer", StringDeserializer.class);
# - props.put("value.deserializer", StringDeserializer.class);
# - KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
# - consumer.subscribe(Collections.singletonList("output-topic"));
# - while (true) {
# -   ConsumerRecords<String, String> records = consumer.poll(100);
# -   for (ConsumerRecord<String, String> record : records) {
# -     System.out.println(record.value());
# -   }
# - }
# Kafka Streams Example: Create a Kafka Streams application to process real-time data.
# Example Kafka Streams code:
# - KStream<String, String> stream = builder.stream("input-topic");
# - stream.mapValues(value -> value.toUpperCase()).to("output-topic");
# Kafka Connect Example: Create a Kafka Connect application to connect Kafka with an external system.
# Example Kafka Connect code:
# - Properties props = new Properties();
# - props.put("bootstrap.servers", "localhost:9092");
# - props.put("key.deserializer", StringDeserializer.class);
# - props.put("value.deserializer", StringDeserializer.class);
# - KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
# - consumer.subscribe(Collections.singletonList("input-topic"));
# - while (true) {
# -   ConsumerRecords<String, String> records = consumer.poll(100);
# -   for (ConsumerRecord<String, String> record : records) {
# -     System.out.println(record.value());
# -   }
# - }