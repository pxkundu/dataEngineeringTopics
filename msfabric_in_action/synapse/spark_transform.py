```

---

## 3. Synapse Spark Transformation Script

**File: synapse/spark_transform.py**

```python
from pyspark.sql import SparkSession

# Initialize Spark session
# This script is run on Synapse Spark for data transformation
spark = SparkSession.builder.appName("TransformSalesData").getOrCreate()

# Load raw sales data from Azure Data Lake (replace <storage_account> and <container> with actual values)
raw_data_path = "abfss://raw@<storage_account>.dfs.core.windows.net/sales_data/"
raw_df = spark.read.json(raw_data_path)  # Read JSON files

# Show the first few rows of raw data for debugging
raw_df.show()

# Transform the data by calculating total sales by region and product
sales_summary = raw_df.groupBy("region", "product").sum("amount")

# Rename the aggregated column for clarity
sales_summary = sales_summary.withColumnRenamed("sum(amount)", "total_sales")

# Show the transformed data for debugging
sales_summary.show()

# Save the transformed data back to Azure Data Lake
processed_data_path = "abfss://processed@<storage_account>.dfs.core.windows.net/sales_summary/"
sales_summary.write.mode("overwrite").parquet(processed_data_path)

print("Data transformation completed successfully.")
```

---

## 4. Power BI Setup Instructions

**File: power_bi/setup_instructions.md**

### Instructions to Create Power BI Dashboard

1. **Connect Power BI to Azure Data Lake**:
   - Open Power BI Desktop.
   - Select **Get Data > Azure Data Lake Storage Gen2**.
   - Enter the storage account details and navigate to the `processed/sales_summary` folder.

2. **Load Transformed Data**:
   - Select the Parquet file containing the aggregated sales data.
   - Click **Load** to import the data into Power BI.

3. **Create Visualizations**:
   - **Bar Chart**:
     - Axis: `region`
     - Values: `total_sales`
   - **Pie Chart**:
     - Legend: `product`
     - Values: `total_sales`

4. **Customize the Dashboard**:
   - Add titles, labels, and filters as needed.

5. **Publish the Dashboard**:
   - Sign in to your Power BI account.
   - Select **Publish** and choose your Power BI workspace.

---

## 5. Azure Data Factory Pipeline Configuration

**File: data_factory/kafka_to_datalake.json**

```json
{
  "name": "KafkaToDataLakePipeline",
  "properties": {
    "activities": [
      {
        "name": "IngestKafkaData",
        "type": "Copy",
        "inputs": [
          { "referenceName": "KafkaSource", "type": "DatasetReference" }
        ],
        "outputs": [
          { "referenceName": "DataLakeSink", "type": "DatasetReference" }
        ]
      }
    ]
  }
}
```

**File: data_factory/setup_instructions.md**

### Azure Data Factory Pipeline Setup

1. **Create a Linked Service for Kafka**:
   - Go to **Manage > Linked Services** in Azure Data Factory.
   - Add a new Linked Service for Kafka and configure the connection.

2. **Create a Linked Service for Data Lake Storage**:
   - Add a new Linked Service for Azure Data Lake Storage Gen2.

3. **Create the Pipeline**:
   - Import the JSON configuration file (`kafka_to_datalake.json`).
   - Test the pipeline by running it manually to verify data ingestion.

---

This set of project files includes detailed comments and step-by-step guidance to help you understand and implement the Real-Time Sales Analytics Pipeline. Let me know if you need additional clarification or adjustments! 🚀
