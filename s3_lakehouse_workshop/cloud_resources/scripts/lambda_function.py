import boto3
import os
import json
from datetime import datetime

# Initialize AWS clients
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

# Environment variables
PROCESSED_TABLE_NAME = os.getenv("PROCESSED_TABLE_NAME")
INSIGHTS_TABLE_NAME = os.getenv("INSIGHTS_TABLE_NAME")


def handler(event, context):
    """
    Lambda function triggered by S3 upload event.
    Processes the file and dynamically updates insights in DynamoDB.
    """
    for record in event["Records"]:
        bucket_name = record["s3"]["bucket"]["name"]
        object_key = record["s3"]["object"]["key"]

        print(f"Processing file {object_key} from bucket {bucket_name}")

        # Skip non-raw files
        if not object_key.startswith("raw/"):
            print(f"Skipping non-raw file: {object_key}")
            continue

        # Download and parse raw data
        raw_data = s3.get_object(Bucket=bucket_name, Key=object_key)["Body"].read().decode("utf-8")

        try:
            raw_records = json.loads(raw_data)
            if not isinstance(raw_records, list):
                raise ValueError("Raw data must be a list of records.")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error parsing file {object_key}: {e}")
            continue

        # Process each record
        processed_records = []
        for record in raw_records:
            if not validate_record(record):
                print(f"Invalid record format: {record}")
                continue

            # Process and store data
            processed_record = process_data(record)
            processed_records.append(processed_record)

            # Update insights in DynamoDB dynamically
            store_in_dynamodb(PROCESSED_TABLE_NAME, processed_record)
            update_insights(record)

        # Write processed records to S3
        if processed_records:
            processed_key = write_to_s3(bucket_name, processed_records)
            print(f"Processed data saved to {processed_key}")


def validate_record(record):
    """
    Validate the structure of a raw record.
    """
    required_keys = {"user_id", "event_type", "product", "timestamp"}
    return isinstance(record, dict) and required_keys.issubset(record.keys())


def process_data(record):
    """
    Process raw data and return structured data.
    """
    return {
        "data_id": f"{record['user_id']}-{record['timestamp']}",
        "user_id": record["user_id"],
        "event_type": record["event_type"],
        "product": record["product"],
        "timestamp": record["timestamp"],
        "processed_at": datetime.utcnow().isoformat(),
    }

def update_insights(record):
    """
    Dynamically update insights in DynamoDB.
    """
    table = dynamodb.Table(INSIGHTS_TABLE_NAME)
    user_id = record["user_id"]
    event_type = record["event_type"]

    try:
        # Increment the count for the specific user and event type
        table.update_item(
            Key={
                "metric_type": event_type,  # Partition Key
                "metric_key": user_id       # Sort Key
            },
            UpdateExpression="SET #count = if_not_exists(#count, :start) + :increment",
            ExpressionAttributeNames={
                "#count": "count"
            },
            ExpressionAttributeValues={
                ":start": 0,
                ":increment": 1
            }
        )
        print(f"Updated insights for user_id={user_id}, event_type={event_type}")
    except Exception as e:
        print(f"Error updating insights: {e}")

def write_to_s3(bucket_name, processed_records):
    """
    Write processed data to the processed/ folder in S3.
    """
    processed_key = f"processed/date={datetime.utcnow().strftime('%Y-%m-%d')}/processed_data_{int(datetime.utcnow().timestamp())}.json"
    processed_data = json.dumps(processed_records)
    s3.put_object(Bucket=bucket_name, Key=processed_key, Body=processed_data)
    return processed_key               

def store_in_dynamodb(table_name, item):
    """
    Store an item in the specified DynamoDB table.
    """
    if not table_name:
        raise ValueError("Table name must be defined")
    table = dynamodb.Table(table_name)
    table.put_item(Item=item)
    print(f"Stored item in {table_name}: {item}")
