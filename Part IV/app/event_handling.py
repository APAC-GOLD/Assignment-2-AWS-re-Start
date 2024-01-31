# Event Handler
# contain functions related to EventBridge operations,
# such as the send_event function.

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
bucket_name = boto3.client("supercalifragailisticexpialidociou5")

eventbridge_client = boto3.client("s3")
EVENT_BUS_NAME = "image-processing-bus"

from image_processing import resize_image
from s3_operations import upload_image, create_presigned_url
from event_handling import send_event


def notify_resize_fail_function(event, context):
    # Failure notification code here
    detail = json.loads(event['detail'])
    error = detail['error']
    # Here you can add code to handle the failure event, such as sending an alert
    print(f"Image processing failed. Error: {error}")


def notify_resize_success_function(event, context):
    # Success notification code here
    detail = json.loads(event['detail'])
    url = detail['url']
    # Here you can add code to handle the success event, such as sending a notification
    print(f"Image processing succeeded. Resized image URL: {url}")
