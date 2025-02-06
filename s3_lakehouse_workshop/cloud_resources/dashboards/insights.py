import boto3
from collections import defaultdict

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Connect to Insights Table
INSIGHTS_TABLE_NAME = 'DynamoDBStack-InsightsTableBE354BC6-15SIZYEUQY4UK'
insights_table = dynamodb.Table(INSIGHTS_TABLE_NAME)

def aggregate_insights_by_event_type():
    """
    Aggregates insights by event type and user from the DynamoDB InsightsTable.
    Returns a list of dictionaries with user, event_type, and count.
    """
    # Scan the InsightsTable to retrieve all data
    response = insights_table.scan()
    items = response.get('Items', [])

    # Aggregate the data
    aggregated_data = []
    for item in items:
        aggregated_data.append({
            "user": item['metric_key'],         # user_id
            "event_type": item['metric_type'],  # event_type
            "count": int(item['count'])         # Interaction count
        })

    return aggregated_data


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
