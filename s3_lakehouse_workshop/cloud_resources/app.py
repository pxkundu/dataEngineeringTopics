#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.data_pipeline_stack import DataPipelineStack
from stacks.dynamodb_stack import DynamoDBStack
from stacks.athena_stack import AthenaStack

app = cdk.App()

    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html


# Create DynamoDB Stack
dynamodb_stack = DynamoDBStack(app, "DynamoDBStack")

# Create Data Pipeline Stack (requires DynamoDB tables)
data_pipeline_stack = DataPipelineStack(
    app,
    "DataPipelineStack",
    processed_table=dynamodb_stack.processed_data_table,
    insights_table=dynamodb_stack.insights_table,
)

# Create Athena Stack (requires S3 bucket from Data Pipeline Stack)
athena_stack = AthenaStack(
    app,
    "AthenaStack",
    s3_bucket=data_pipeline_stack.s3_bucket,
)

app.synth()