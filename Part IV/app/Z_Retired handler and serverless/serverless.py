# handler warmfuzzies v5
import uuid
import json
from urllib.parse import unquote_plus
import boto3
from PIL import Image
import botocore
import logging
import os

# Get the bucket names from environment variables
PHOTOS_BUCKET = os.getenv("photos-yma/uploads")
PROCESSED_BUCKET = os.getenv("supercalifragailisticexpialidociou5/processed")
THUMBNAILS_FOLDER = os.getenv("photos-yma/thumbnails")


service: app
frameworkVersion: "3"
provider:
    name: aws
    runtime: "3.12"
    region: us-east-1
  environment:
    S3_BUCKET_NAME: "photos-yma"
  iamRoleStatements:
    - Effect: Allow
      Action:
        - s3:GetObject
        - s3:PutObject
      Resource:
        - "arn:aws:s3:::${self:provider.environment.S3_BUCKET_NAME}/*"

functions:
  process_image_function:
    handler: handler.process_image
    events:
      - s3:
          bucket: "${self:provider.environment.S3_BUCKET_NAME}"
          event: s3:ObjectCreated:*
          rules:
            - prefix: uploads/
            - suffix: .jpg
  notify_resize_success_function:
    handler: handler.notify_resize_success
  notify_resize_fail_function:
    handler: handler.notify_resize_fail

plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: true