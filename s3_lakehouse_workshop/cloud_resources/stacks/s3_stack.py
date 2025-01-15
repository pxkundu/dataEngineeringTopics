from aws_cdk import aws_s3 as s3
from aws_cdk import Stack
from constructs import Construct

class S3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define S3 bucket
        self.s3_bucket = s3.Bucket(
            self,
            "EcommerceDataLake",
            bucket_name="ecommerce-data-lakehouse",
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )
