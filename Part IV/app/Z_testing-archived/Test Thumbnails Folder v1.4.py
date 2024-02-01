# Test Thumbnail Folder v1.4
import boto3
from moto import mock_s3
from handler import create_thumbnail


@mock_s3
def test_create_thumbnail():
    """
    This function sets up a mock S3, uploads a test image to the mock S3 bucket,
    creates a mock event, calls the create_thumbnail function with the mock event,
    and checks that the thumbnail was created.
    """
    # Set up mock S3
    conn = boto3.resource("s3", region_name="us-east-1")
    conn.create_bucket(Bucket="photos-yma")

    # Upload a test image to the mock S3 bucket
    with open("test_image.jpg", "rb") as data:
        conn.Bucket("photos-yma").put_object(Key="uploads/test_image.jpg", Body=data)

    # Create a mock event
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": "photos-yma"},
                    "object": {"key": "uploads/test_image.jpg"},
                }
            }
        ]
    }

    # Call the function with the mock event
    create_thumbnail(event, None)

    # Check that the thumbnail was created
    assert conn.Object("photos-yma", "thumbnails/test_image.jpg").get()

    # Check thumbnail
    assert conn.Object("photos-yma", "thumbnails/test_image.jpg").get()

    # Check original
    assert conn.Object("photos-yma", "uploads/test_image.jpg").get()


# Call the test function
test_create_thumbnail()
