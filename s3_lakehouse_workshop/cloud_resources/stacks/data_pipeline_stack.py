from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3_notifications as s3n
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_iam as iam
from aws_cdk import Stack
from constructs import Construct
from aws_cdk.aws_dynamodb import Table

class DataPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, processed_table: Table, insights_table: Table, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create S3 bucket
        self.s3_bucket = s3.Bucket(
            self,
            "EcommerceDataLake",
            bucket_name="ecommerce-data-lakehouse",
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        # Create Lambda function
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

        # Grant permissions to the Lambda function
        self.s3_bucket.grant_read(self.lambda_function)  # Allow reading from S3 bucket
        self.s3_bucket.grant_put(self.lambda_function)   # Allow writing to S3 bucket

        # Additional permissions for specific prefixes (optional, more secure)
        self.lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["s3:PutObject"],
                resources=[
                    f"{self.s3_bucket.bucket_arn}/processed/*"  # Grant access to the processed folder
                ]
            )
        )

        # Grant permissions for DynamoDB tables
        processed_table.grant_write_data(self.lambda_function)
        insights_table.grant_write_data(self.lambda_function)

        # Add S3 trigger for raw data uploads
        self.s3_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(self.lambda_function)
        )
