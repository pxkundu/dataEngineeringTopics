import boto3
from collections import defaultdict

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Connect to Insights Table
INSIGHTS_TABLE_NAME = 'DynamoDBStack-InsightsTableBE354BC6-1SZHT57IRKVQY'
insights_table = dynamodb.Table(INSIGHTS_TABLE_NAME)

def aggregate_insights():
    """
    Aggregates insights data from the DynamoDB InsightsTable.
    Returns a dictionary where keys are user IDs and values are total interaction counts.
    """
    # Scan the table to retrieve all data
    response = insights_table.scan()
    items = response.get('Items', [])

    # Aggregate the data by user
    aggregated_data = defaultdict(int)
    for item in items:
        user_id = item['metric_key']  # Assuming 'metric_key' is user_id
        count = int(item['count'])
        aggregated_data[user_id] += count

    return [{"user": user, "count": count} for user, count in aggregated_data.items()]
