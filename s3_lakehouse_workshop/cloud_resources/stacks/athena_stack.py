from aws_cdk import aws_s3 as s3
from aws_cdk import Stack, Duration
from constructs import Construct
from aws_cdk.aws_s3 import IBucket

class AthenaStack(Stack):
    def __init__(self, scope: Construct, id: str, s3_bucket: IBucket, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Add a lifecycle rule for Athena query results
        s3_bucket.add_lifecycle_rule(
            id="AthenaQueryResults",
            prefix="athena-results/",
            expiration=Duration.days(30),  # Automatically delete results after 30 days
        )
