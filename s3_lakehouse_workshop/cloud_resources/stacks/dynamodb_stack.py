from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import Stack
from constructs import Construct

class DynamoDBStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Processed Data Table
        self.processed_data_table = dynamodb.Table(
            self,
            "ProcessedDataTable",
            partition_key=dynamodb.Attribute(
                name="data_id",
                type=dynamodb.AttributeType.STRING,
            ),
        )

        # Insights Table
        self.insights_table = dynamodb.Table(
            self,
            "InsightsTable",
            partition_key=dynamodb.Attribute(
                name="metric_type",
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name="metric_key",
                type=dynamodb.AttributeType.STRING,
            ),
        )
