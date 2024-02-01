import uuid
from urllib.parse import unquote_plus
import boto3
from PIL import Image


s3_client = boto3.client("s3")


def calculate_resized_height(original_width, original_height, new_width):
    return int(original_height * (new_width / original_width))


def resize_image(image_path, resized_path):
    with Image.open(image_path) as img:
        width, height = img.size
        print(f"Original image size: {img.size}")

        if width <= 200:
            img.save(resized_path)
            return

        new_width = 200
        new_height = calculate_resized_height(width, height, new_width)

        img = img.resize((new_width, new_height))
        img.save(resized_path)

        print(f"Resized image size: {img.size}")


def supercalifragilisticexpialidociou5(event, context):
    for record in event["Records"]:
        try:
            bucket_name = record["s3"]["bucket"]["name"]
            original_s3_path = unquote_plus(record["s3"]["object"]["key"])
            filename = original_s3_path.split("/")[-1]
            print(f"The image name is s3://{bucket_name}/uploads/{filename}")
            print(f"The thumbnail name is s3://{bucket_name}/thumbnails/{filename}")
            local_download_path = f"/tmp/{uuid.uuid4()}{filename}"
            print(f"The local image name is {local_download_path}")
            local_upload_path = f"/tmp/resized-{filename}"
            print(f"The local thumbnail name is {local_upload_path}")
            s3_client.download_file(
                bucket_name, f"uploads/{filename}", local_download_path
            )
            resize_image(local_download_path, local_upload_path)
            s3_client.upload_file(
                local_upload_path, bucket_name, f"thumbnails/{filename}"
            )
            print("SUCCEEDED")
        except Exception as ex:
            print("FAILED")
            print("Error processing image: ", ex)
            raise
