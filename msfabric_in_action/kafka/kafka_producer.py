## 1. Kafka Producer Script

#File: kafka/kafka_producer.py**

from kafka import KafkaProducer
import json
import time
import random

# Kafka Producer setup
# The producer will send data to the Kafka topic 'sales_topic' hosted on localhost
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka server address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize Python dictionary to JSON bytes
)

# Function to simulate sales data
def generate_sales_data():
    # Define some example products and regions
    products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor']
    regions = ['North America', 'Europe', 'Asia']

    while True:
        # Generate a random sales record
        sale = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),  # Current timestamp
            "region": random.choice(regions),  # Random region
            "product": random.choice(products),  # Random product
            "amount": round(random.uniform(100, 1000), 2)  # Random sales amount
        }
        # Send the record to the Kafka topic
        producer.send('sales_topic', value=sale)
        print(f"Produced: {sale}")  # Log the record for debugging
        time.sleep(1)  # Wait 1 second before sending the next record

if __name__ == "__main__":
    generate_sales_data()  # Start generating sales data
