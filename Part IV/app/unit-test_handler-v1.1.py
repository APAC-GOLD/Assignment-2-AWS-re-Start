import boto3
from moto import mock_s3
from handler import create_thumbnail


@mock_s3
def test_create_thumbnail():
    # Set up mock S3
    conn = boto3.resource("s3", region_name="us-east-1")
    conn.create_bucket(Bucket="mybucket")

    # Upload a test image to the mock S3 bucket
    with open("test_image.jpg", "rb") as data:
        conn.Bucket("mybucket").put_object(Key="uploads/test_image.jpg", Body=data)

    # Create a mock event
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": "mybucket"},
                    "object": {"key": "uploads/test_image.jpg"},
                }
            }
        ]
    }

    # Call the function with the mock event
    create_thumbnail(event, None)

    # Check that the thumbnail was created
    assert conn.Object("mybucket", "thumbnails/test_image.jpg").get()


test_create_thumbnail()
