"""Uploads a file to the bucket the customer portal reads from."""

import boto3

BUCKET = "billing-documents"
client = boto3.client("s3")


def upload(key: str, body: bytes) -> None:
    client.put_object(Bucket=BUCKET, Key=key, Body=body)
