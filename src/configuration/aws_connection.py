import boto3
from src.constants import REGION_NAME


class S3Client:
    """
    Production-ready S3 Client.

    Credential Resolution Order (handled automatically by boto3):

    1) Environment Variables (if present)
    2) ~/.aws/credentials (aws configure)
    3) IAM Role (EC2/ECS/Cloud)

    NO manual credential handling required.
    """

    def __init__(self, region_name=REGION_NAME):

        try:
            # Create S3 Resource
            self.s3_resource = boto3.resource(
                service_name="s3",
                region_name=region_name
            )

            # Create S3 Client
            self.s3_client = boto3.client(
                service_name="s3",
                region_name=region_name
            )

            # Validate AWS Authentication (Fail Fast)
            boto3.client("sts").get_caller_identity()

        except Exception as e:
            raise Exception(f"AWS S3 Initialization Failed: {str(e)}")
