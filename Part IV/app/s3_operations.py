
# s3_operations.py

# module contain functions related to S3 operations, such as the 
# upload_image and create_presigned_url functions.

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
EVENT_BUS_NAME = "image-processing-bus"

Remember to import the necessary modules in your handler.py file. For example:
from image_processing import resize_image
from s3_operations import upload_image, create_presigned_url
from event_handling import send_event


# S3 Put Object
def put_s3_image(bucket_name, key, image):
    # Code to put the resized image back to S3
    s3_client.upload_file(image, bucket_name, f"thumbnails/{key}")



# Get Image 

def get_s3_image(bucket, key):
    try:
        original_s3_path = unquote_plus(event["detail"]["s3"]["object"]["key"])
        print(f"The image name is s3://{bucket_name}/{original_s3_path}")
        tmpkey = original_s3_path.replace("/", "")
        local_download_path = "/tmp/{}{}".format(uuid.uuid4(), tmpkey)
        s3_client.download_file(bucket_name, original_s3_path, local_download_path)
    except botocore.exceptions.ClientError as inner_e:
        if inner_e.response["Error"]["Code"] == "404":
            print("The object does not exist.")
        else:
            raise
        

def get_s3_image(bucket, key):
    # Get the image from S3
    try:
        original_s3_path = unquote_plus(event["detail"]["s3"]["object"]["key"])
        print(f"The image name is s3://{bucket_name}/{original_s3_path}")
        tmpkey = original_s3_path.replace("/", "")
        local_download_path = "/tmp/{}{}".format(uuid.uuid4(), tmpkey)
        s3_client.download_file(bucket_name, original_s3_path, local_download_path)
    except botocore.exceptions.ClientError as inner_e:
        if inner_e.response["Error"]["Code"] == "404":
            print("The object does not exist.")
        else:
            raise