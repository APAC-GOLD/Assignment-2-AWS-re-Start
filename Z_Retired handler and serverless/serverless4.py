import uuid
import json
from urllib.parse import unquote_plus
import boto3
from PIL import Image

s3_client = boto3.client("s3")
eventbridge_client = boto3.client("events")
EVENT_BUS_NAME = "image-processing-bus"


def resize_image(image_path, resized_path):
    with Image.open(image_path) as img:
        width, height = img.size
        if width <= 200:
            img.save(resized_path)
            return
        new_width = 200
        new_height = int(height * (new_width / width))
        img = img.resize((new_width, new_height))
        img.save(resized_path)


def process_image(event, context):
    for record in event["Records"]:
        try:
            bucket_name = record["s3"]["bucket"]["name"]
            original_s3_path = unquote_plus(record["s3"]["object"]["key"])
            filename = original_s3_path.split("/")[-1]
            local_download_path = f"/tmp/{uuid.uuid4()}{filename}"
            local_upload_path = f"/tmp/resized-{filename}"
            s3_client.download_file(
                bucket_name, f"uploads/{filename}", local_download_path
            )
            resize_image(local_download_path, local_upload_path)
            s3_client.upload_file(
                local_upload_path, "warmfuzzies", f"processed/{filename}"
            )
            send_success_event(f"processed/{filename}")
        except Exception as ex:
            send_fail_event(str(ex))


def send_success_event(key):
    eventbridge_client.put_events(
        Entries=[
            {
                "Source": "custom.myApp",
                "DetailType": "ImageProcessing",
                "Detail": json.dumps(
                    {"status": "SUCCEEDED", "url": f"s3://warmfuzzies/processed/{key}"}
                ),
                "EventBusName": EVENT_BUS_NAME,
            }
        ]
    )


def send_fail_event(error):
    eventbridge_client.put_events(
        Entries=[
            {
                "Source": "custom.myApp",
                "DetailType": "ImageProcessing",
                "Detail": json.dumps({"status": "FAILED", "error": error}),
                "EventBusName": EVENT_BUS_NAME,
            }
        ]
    )


def notify_resize_success_function(event, context):
    detail = json.loads(event["detail"])
    url = detail["url"]
    print(f"Image processing succeeded. Resized image URL: {url}")


def notify_resize_fail_function(event, context):
    detail = json.loads(event["detail"])
    error = detail["error"]
    print(f"Image processing failed. Error: {error}")
