# test.py
# write tests for the functions in the:
# image_processing, s3_operations, handler, and event_handling modules.
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
