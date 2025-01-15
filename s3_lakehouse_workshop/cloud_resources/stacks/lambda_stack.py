from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3_notifications as s3n
from aws_cdk import aws_s3 as s3
from aws_cdk import Stack
from constructs import Construct
from aws_cdk.aws_dynamodb import Table

class LambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, s3_bucket: s3.IBucket, processed_table: Table, insights_table: Table, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define Lambda function
        self.lambda_function = _lambda.Function(
            self,
            "DataProcessor",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("scripts/"),
            environment={
                "PROCESSED_TABLE_NAME": processed_table.table_name,
                "INSIGHTS_TABLE_NAME": insights_table.table_name,
            }
        )

        # Grant permissions
        s3_bucket.grant_read(self.lambda_function)
        processed_table.grant_write_data(self.lambda_function)
        insights_table.grant_write_data(self.lambda_function)

        # Add S3 trigger
        s3_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,  # Fixed import for event type
            s3n.LambdaDestination(self.lambda_function)
        )
