Here’s a detailed `README.md` for your `cloud_resources` folder:

---

# **Cloud Resources - AWS CDK Configuration and Deployment Guide**

This folder contains the AWS CDK configuration files for deploying the cloud infrastructure required for the project. The infrastructure includes the following resources:
- **S3 Buckets** for storing raw and processed data.
- **DynamoDB Tables** for storing processed data and insights.
- **Lambda Functions** for data processing and insights generation.
- **Athena** for querying processed data.
- Other supporting AWS resources.

This guide provides a step-by-step process to configure the AWS CLI, CDK, and deploy the infrastructure.

---

## **Table of Contents**
1. [Prerequisites](#prerequisites)
2. [AWS CLI Configuration](#aws-cli-configuration)
3. [CDK Setup](#cdk-setup)
4. [Project Structure](#project-structure)
5. [Deploying the CDK Stack](#deploying-the-cdk-stack)
6. [Testing the Deployment](#testing-the-deployment)
7. [Useful CDK Commands](#useful-cdk-commands)

---

## **1. Prerequisites**

Before proceeding, ensure you have the following installed on your system:
1. **Node.js** (v16 or higher): [Install Node.js](https://nodejs.org/).
2. **AWS CLI** (v2 or higher): [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
3. **Python** (v3.7 or higher): [Install Python](https://www.python.org/).
4. **AWS CDK** (v2): Installed via npm.

---

## **2. AWS CLI Configuration**

### Step 1: Configure AWS CLI
Run the following command to configure the AWS CLI:
```bash
aws configure
```

You will be prompted to enter:
- **AWS Access Key ID**: Obtain this from the AWS IAM Console.
- **AWS Secret Access Key**: Obtain this from the AWS IAM Console.
- **Default region**: Example: `us-east-1`
- **Default output format**: Example: `json`

Verify your configuration:
```bash
aws sts get-caller-identity
```

---

## **3. CDK Setup**

### Step 1: Install AWS CDK
Install the AWS CDK globally using npm:
```bash
npm install -g aws-cdk
```

Verify the installation:
```bash
cdk --version
```

### Step 2: Set Up a Python Virtual Environment
Navigate to the `cloud_resources` folder:
```bash
cd cloud_resources
```

Set up a Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Step 3: Bootstrap AWS CDK
Bootstrap the environment to prepare it for deploying AWS resources:
```bash
cdk bootstrap aws://<AWS_ACCOUNT_ID>/<AWS_REGION>
```
Replace `<AWS_ACCOUNT_ID>` with your AWS account ID and `<AWS_REGION>` with your desired region.

---

## **4. Project Structure**

The `cloud_resources` folder contains the following files and directories:

```
cloud_resources/
├── README.md               # Documentation for the CDK project
├── app.py                  # Main entry point for the CDK application
├── cdk.json                # CDK configuration file
├── requirements.txt        # Python dependencies for the project
├── stacks/                 # Directory containing CDK stack definitions
│   ├── data_pipeline_stack.py  # Defines S3, Lambda resources
│   ├── dynamodb_stack.py       # Defines DynamoDB tables
│   ├── athena_stack.py         # Defines Athena setup
└── scripts/               # Lambda function code
```

---

## **5. Deploying the CDK Stack**

Follow these steps to deploy the AWS infrastructure using CDK.

### Step 1: Synthesize the CloudFormation Template
Run the following command to generate the CloudFormation template:
```bash
cdk synth
```

This will output the CloudFormation template that CDK will use to deploy the resources.

### Step 2: Deploy the Stack
Deploy all the stacks in the project:
```bash
cdk deploy --all
```

You will be prompted to confirm the creation of the resources. Type `y` to proceed.

---

## **6. Testing the Deployment**

### Verify Resources
1. **S3 Buckets**:
   - Navigate to the S3 Console and verify that the `ecommerce-data-lakehouse` bucket has been created.
   - Check the `raw/` and `processed/` folders.

2. **DynamoDB Tables**:
   - Verify the `ProcessedDataTable` and `InsightsTable` in the DynamoDB Console.
   - Check that they have the correct partition and sort keys.

3. **Lambda Functions**:
   - Navigate to the Lambda Console and verify the function `DataProcessor`.
   - Check its environment variables (`PROCESSED_TABLE_NAME`, `INSIGHTS_TABLE_NAME`).

4. **Athena**:
   - Verify the Athena query results location in the S3 bucket.

### Trigger the Lambda Function
Upload a sample JSON file to the `raw/` folder in the S3 bucket. The Lambda function should process the data and:
- Write processed data to the `processed/` folder.
- Update metrics in the `InsightsTable`.

Monitor the function's logs in **CloudWatch**.

---

## **7. Useful CDK Commands**

### Synthesizing the CloudFormation Template
```bash
cdk synth
```

### Deploying the Stacks
```bash
cdk deploy --all
```

### Destroying the Stacks
To delete all deployed resources:
```bash
cdk destroy --all
```

### Listing Stacks
To list all available stacks in the project:
```bash
cdk list
```

### Checking Differences
To compare your app with the deployed stacks:
```bash
cdk diff
```

---

## **Troubleshooting**

- **Access Denied Errors**:
  Ensure the IAM role used for CDK deployment has sufficient permissions to create the required resources.

- **Stack Rollback**:
  Check the **CloudFormation Console** for detailed error messages and resolve the issues before re-deploying.

---

This guide should help developers set up and deploy the AWS infrastructure using CDK seamlessly. If you encounter any issues, feel free to reach out for support.

--- 
