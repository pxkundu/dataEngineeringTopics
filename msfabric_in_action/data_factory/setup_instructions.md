
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
