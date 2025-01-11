

### **Explanation of the Configuration**
1. **Pipeline Name**:
   - `"name": "SalesDataTransformationPipeline"` specifies the name of the pipeline.

2. **Activities**:
   - The pipeline runs a **Notebook activity** called `RawToProcessedData`.
   - The notebook references `transform_data` to handle the data transformation process.

3. **Linked Services**:
   - `"linkedServiceName": "SynapseSparkPool"` points to the Synapse Spark pool where the notebook will run.

4. **Parameters**:
   - `"rawDataPath"`: Path to the raw data in the Data Lake.
   - `"processedDataPath"`: Destination path for the transformed data.

5. **Retry Policy**:
   - Configured with up to 3 retries and a timeout of 10 minutes.

6. **Integration Runtime**:
   - Uses the default Azure-managed integration runtime for executing the pipeline.

---

### **Steps to Use**
1. **Create the Pipeline**:
   - Open **Azure Synapse Studio**.
   - Navigate to **Integrate > + New Pipeline**.
   - Import this `pipeline_config.json` file.

2. **Update Placeholder Values**:
   - Replace `<storage_account>` with your Azure storage account name.

3. **Test the Pipeline**:
   - Trigger the pipeline and verify that the raw data is transformed and saved in the processed folder.

---
