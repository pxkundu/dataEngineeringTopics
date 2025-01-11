
## 2. Kafka Setup Script

##File: kafka/kafka_setup.sh**

#!/bin/bash

# This script sets up the Kafka topic for sales data ingestion
# Ensure Kafka and Zookeeper services are running before executing this script

# Create a Kafka topic named 'sales_topic'
kafka-topics.sh --create \
  --topic sales_topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1

echo "Kafka topic 'sales_topic' created successfully."
