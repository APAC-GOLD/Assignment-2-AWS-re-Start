# handler photos-yma v6

import uuid
import json
from urllib.parse import unquote_plus
import boto3
from PIL import Image
from botocore.exceptions import NoCredentialsError
from botocore.exceptions import ClientError
import io
import os

# Get the bucket names from environment variables
PHOTOS_BUCKET = os.getenv("s3://{bucket_name}/uploads/{filename}")
PROCESSED_BUCKET = os.getenv("s3://{bucket_name}/processed/{filename}")
THUMBNAILS_FOLDER = os.getenv("s3://{bucket_name}/thumbnails/{filename}")

bucket_name = boto3.client("s3 bucket name")
s3_client = boto3.client("s3")
eventbridge_client = boto3.client("events")
EVENT_BUS_NAME = "image-processing-bus"


def put_s3_image(key, image):
    # Code to put the resized image back to S3
    s3_client.upload_file(image, "supercalifragailisticexpialidociou5", key)
  
            
def calculate_resized_height(original_width, original_height, new_width):
    # Code to calculate the image hight after resizing to a new width (thumbnail)
    return int(original_height * (new_width / original_width))


# Resize the image and save it back to S3
def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width} wide x {height} tall")

    if width > size:
        max_width = size
        max_height = height * max_width // width
        original_image.thumbnail((max_width, max_height), Image.ANTIALIAS)
    else:
        print("Image width is less than 200px. No resizing needed.")

    original_image.save(output_image_path)
    print(f"The processed image is saved at {output_image_path}")
        
        
#  Code to upload the resized image to S3
def create_thumbnail(event, context):
    for record in event["Records"]:
        try:
            bucket_name = record["s3"]["bucket"]["name"]
            original_s3_path = unquote_plus(record["s3"]["object"]["key"])
            filename = original_s3_path.split("/")[-1]
            print(f"The image name is s3://{bucket_name}/uploads/{filename}")
            print(f"The processed image name is s3://{bucket_name}/processed/{filename}")
            local_download_path = f"/tmp/{uuid.uuid4()}{filename}"
            print(f"The local image name is {local_download_path}")
            local_upload_path = f"/tmp/resized-{filename}"
            print(f"The local processed image name is {local_upload_path}")
            s3_client.download_file(
            bucket_name, f"uploads/{filename}", local_download_path
            )
            resize_image(local_download_path, local_upload_path, 200)
            s3_client.upload_file(
                local_upload_path, bucket_name, f"processed/{filename}"
            )
            print("SUCCEEDED")
        except Exception as ex:
            print("FAILED")
            print("Error processing image: ", ex)
            raise
 
      
def notify_resize_success_function(event, context):
    # Success notification code here
    detail = json.loads(event['detail'])
    url = detail['url']
    # Here you can add code to handle the success event, such as sending a notification
    print(f"Image processing succeeded. Resized image URL: {url}")


def notify_resize_fail_function(event, context):
    # Failure notification code here
    detail = json.loads(event['detail'])
    error = detail['error']
    # Here you can add code to handle the failure event, such as sending an alert
    print(f"Image processing failed. Error: {error}")

   
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
        

    s3_client.upload_file(
        local_upload_path, bucket_name, f"thumbnails/{filename}"
    )
    print("SUCCEEDED")

    # Put a success event to EventBridge
    eventbridge_client.put_events(
        Entries=[
            {
                'Source': 'custom.myApp',
                'DetailType': 'ImageProcessing',
                'Detail': json.dumps({
                    'status': 'SUCCEEDED',
                    'url': f"s3://{bucket_name}/thumbnails/{filename}"
                }),
                'EventBusName': 'image-processing-bus'
            }
        ]
    )


    except Exception as ex:
    print("FAILED")
    print("Error processing image: ", ex)

# Put a failure event to EventBridge
eventbridge_client.put_events(
    Entries=[
        {
            'Source': 'custom.myApp',
            'DetailType': 'ImageProcessing',
            'Detail': json.dumps({
                'status': 'FAILED',
                'error': str(ex)  # Add any additional information you want here

            }),
            'EventBusName': 'image-processing-bus'
        }
    ]
)
raise


      
  # REQUIREMENT  
""" ## Part IV.1. Setup source events 
1. User uploads a high resolution `.jpg` image into the AWS Console into a S3 bucket (you are free to choose the Bucket name), under folder `uploads/`.
2. S3 has been configured to send events to EventBridge. This is your default event bus (all AWS accounts have one). 
3. Setup an EventBridge rule to only listen for files inserted into the `uploads/` folder, suffix file extension is `.jpg` and S3 objects that have been Created.
4. Custom code in a `Lambda function: process-image-function` picks up the events, and resize the image into maximum width of 200 pixels, while keeping the same images ratio (and leave same if the image size is too small). 

## Part IV.2. Checking in

5. Custom code in a `Lambda function: process-image-function` saves this image to a different S3 bucket of your own choosing, under folder `processed/`.
6. Custom code in a `Lambda function: process-image-function` , EventBridge events are sent to custom domain event bus in EventBridge `EventBridge bus: image-processing-bus`. 
7. If the image resizing process and S3 save process completed without error, send an event with `"status": "SUCCEEDED"` to EventBridge bus `EventBridge bus: image-processing-bus`. Additionally, add a publicly shareable S3 presigned URL of them resized image from the new S3 bucket under folder `processed/`. Send this information together with the EventBridge success event.
8. If the image resizing process or S3 save process failed (try except will be needed), send an event with `"status": "FAILED"` to EventBridge bus `EventBridge bus: image-processing-bus`

## Part IV.3. Making a claim

9.  If the EventBridge event typed `"status": "SUCCEEDED"` is sent to EventBridge bus `EventBridge bus: image-processing-bus`, a rule will pick up and send to `Lambda function: notify-resize-success-function` to print out logs `"SUCCEEDED"` and the S3 presigned url path. You can pick this url and test with your browser. 
10.  If the EventBridge event typed `"status":"FAILED"` is sent to EventBridge bus `EventBridge bus: image-processing-bus`, a rule will pick up and send to `Lambda function : notify-resize-fail-function`. This Lambda function can simply logs out `"FAILED"`.

## Part IV.4. Bonus mark for quality

Bonus given for:
- Clean code
- Implementation broken down into modules
- Unit testing with mock S3/EventBridge dependencies
- Python script that makes use of Python SDK to generate test event by uploading to S3 programmatically, or producing mock events to EventBridge
- Figuring out on how to do local development for S3 local/or localstack"""
    