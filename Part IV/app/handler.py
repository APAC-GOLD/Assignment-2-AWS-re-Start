# Handler.py

from s3_operations import upload_image, create_presigned_url
from s3_operations import get_s3_image, put_s3_image
from botocore.exceptions import NoCredentialsError
from botocore.exceptions import ClientError
from image_processing import resize_image
from event_handling import send_event
from urllib.parse import unquote_plus
from PIL import Image
import pydantic as py
import uuid
import json
import boto3
import io
import os
s3_client = boto3.client("s3")
bucket_name = boto3.client("s3 bucket name")
bucket_name = boto3.client("s3 bucket name")
eventbridge_client = boto3.client("events")
EVENT_BUS_NAME = "image-processing-bus"ng-bus"
s3_client = boto3.client("s3")


def lambda_handler(event, context):
    # Get the bucket name and key from the event
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = unquote_plus(event["Records"][0]["s3"]["object"]["key"])

    # Get the image from S3
    image = get_s3_image(bucket, key)

    # Resize the image
    resized_image = resize_image(image)

    # Put the resized image back to S3
    put_s3_image(bucket, key, resized_image)
