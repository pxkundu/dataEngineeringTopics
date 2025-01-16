# **Ecommerce Data Lakehouse Project**

This project demonstrates how to build a **data lakehouse** using AWS services. It includes **data ingestion, processing, storage, and visualization**, showcasing AWS S3, DynamoDB, Lambda, Athena, and Dash for analytics dashboards.

### By: [Partha Sarathi Kundu](https://www.linkedin.com/in/partha-sarathi-kundu/recent-activity/articles/)

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Project Features](#project-features)
4. [Setup Guide](#setup-guide)
   - [Phase 1: Project Initialization](#phase-1-project-initialization)
   - [Phase 2: AWS Infrastructure Setup](#phase-2-aws-infrastructure-setup)
   - [Phase 3: Athena Configuration](#phase-3-athena-configuration)
   - [Phase 4: Dashboard Creation](#phase-4-dashboard-creation)
5. [How to Run the Project](#how-to-run-the-project)
6. [Testing the Project](#testing-the-project)
7. [Troubleshooting](#troubleshooting)
8. [Project Structure](#project-structure)

---

## **1. Project Overview**

This project is designed to simulate an **ecommerce data pipeline** where user interactions are captured, processed, and analyzed using AWS services. The insights gained from the data are visualized on a real-time dashboard for analytics.

---

## **2. Technologies Used**
1. **AWS Services**:
   - **S3**: Data lake storage.
   - **DynamoDB**: NoSQL database for processed data and insights.
   - **Lambda**: Serverless data processing.
   - **Athena**: Interactive query service for analytics.
2. **Python**:
   - For Lambda function logic, data generation, and dashboard development.
3. **Dash by Plotly**:
   - For building an interactive analytics dashboard.
4. **AWS CDK**:
   - For infrastructure as code to define and deploy AWS resources.

---

## **3. Project Features**
1. **Data Ingestion**:
   - Simulated ecommerce user events (e.g., views, clicks) are generated and stored in S3.
2. **Data Processing**:
   - AWS Lambda processes raw data and stores processed data in S3 and DynamoDB.
3. **Data Querying**:
   - Athena enables querying of processed data for advanced analytics.
4. **Visualization**:
   - Dash-based dashboard visualizes insights in real-time.

---

## **4. Setup Guide**

### **Phase 1: Project Initialization**

#### Step 1: Clone the Repository
Clone the project repository to your local system:
```bash
git clone <repository-url>
cd <repository-folder>
```

#### Step 2: Set Up Python Virtual Environment
Create and activate a Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

#### Step 3: Install Python Dependencies
Navigate to the `cloud_resources` folder and install dependencies:
```bash
cd cloud_resources
pip install -r requirements.txt
```

---

### **Phase 2: AWS Infrastructure Setup**

This phase involves setting up the required AWS resources using AWS CDK.

#### Step 1: Configure AWS CLI
Run the following to configure AWS CLI:
```bash
aws configure
```
Provide your **AWS Access Key ID**, **Secret Access Key**, **Default Region**, and **Output Format**.

#### Step 2: Bootstrap AWS CDK
Bootstrap your AWS environment for CDK:
```bash
cdk bootstrap aws://<AWS_ACCOUNT_ID>/<AWS_REGION>
```

#### Step 3: Deploy the CDK Stacks
Deploy the AWS infrastructure using:
```bash
cdk deploy --all
```

**Stacks Deployed**:
1. **S3 Buckets**: For raw and processed data.
2. **DynamoDB Tables**: For processed data and insights.
3. **Lambda Functions**: For data processing.
4. **Athena Query Configuration**: For analytics.

---

### **Phase 3: Athena Configuration**

#### Step 1: Create a Database
Create an Athena database for your queries:
```sql
CREATE DATABASE ecommerce_data_lake;
```

#### Step 2: Create a Table
Create a table in Athena to query processed data stored in S3:
```sql
CREATE EXTERNAL TABLE ecommerce_data_lake.processed_data (
    data_id STRING,
    user_id STRING,
    event_type STRING,
    product STRING,
    timestamp BIGINT,
    processed_at STRING
)
PARTITIONED BY (date STRING)
STORED AS TEXTFILE
LOCATION 's3://ecommerce-data-lakehouse/processed/';
```

#### Step 3: Add Partitions
Manually add partitions to the table for new data:
```sql
ALTER TABLE ecommerce_data_lake.processed_data
ADD PARTITION (date='2025-01-14') LOCATION 's3://ecommerce-data-lakehouse/processed/date=2025-01-14/';
```

---

### **Phase 4: Dashboard Creation**

#### Step 1: Navigate to the Dashboard Folder
Go to the `dashboard/` directory:
```bash
cd ../dashboard
```

#### Step 2: Install Dependencies
Install Python dependencies for the dashboard:
```bash
pip install -r requirements.txt
```

#### Step 3: Run the Dashboard Locally
Start the dashboard:
```bash
python app.py
```

Access the dashboard at:
```
http://127.0.0.1:8050/
```

---

## **5. How to Run the Project**

1. **Start Data Generation**:
   Use the data generator script to populate raw data in S3:
   ```bash
   python scripts/data_generator.py
   ```

2. **Monitor Lambda Processing**:
   - Upload raw data to the `raw/` folder in S3.
   - Check CloudWatch logs for Lambda execution.

3. **Query Data in Athena**:
   Run queries to analyze processed data.

4. **View the Dashboard**:
   Start the dashboard and analyze real-time insights.

---

## **6. Testing the Project**

1. **Data Processing**:
   Upload test JSON files to the `raw/` S3 folder and verify processing in the `processed/` folder.
2. **Athena Queries**:
   Test example queries in Athena to ensure data is correctly partitioned and queryable.
3. **Dashboard Functionality**:
   Verify that both graphs display accurate insights.

---

## **7. Troubleshooting**

1. **AWS CLI Token Expiry**:
   Reauthenticate using:
   ```bash
   aws sso login
   ```

2. **CDK Deployment Issues**:
   Ensure the CDK version matches the stack code:
   ```bash
   cdk --version
   ```

3. **Dashboard Port in Use**:
   If `port 8050` is in use, change the port in `app.py`:
   ```python
   app.run_server(debug=True, port=8051)
   ```

---

## **8. Project Structure**
```plaintext
.
├── README.md                   # Documentation
├── cloud_resources/            # AWS CDK configuration
│   ├── app.py                  # Main entry point for CDK
│   ├── stacks/                 # CDK stack definitions
│   └── requirements.txt        # Dependencies for CDK
├── data/                       # Data folders
│   ├── raw/                    # Raw data (input to Lambda)
│   ├── processed/              # Processed data (output of Lambda)
├── dashboards/                 # Dashboard for analytics
│   ├── app.py                  # Main Dash app
│   ├── insights.py             # Logic for data aggregation
│   └── requirements.txt        # Dependencies for the dashboard
└── scripts/                    # Utility scripts
    ├── data_generator.py       # Script to generate raw data
    └── lambda_function.py      # Lambda function code
```

---

### By: [Partha Sarathi Kundu](https://www.linkedin.com/in/partha-sarathi-kundu/recent-activity/articles/)
