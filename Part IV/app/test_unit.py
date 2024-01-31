# Test Unit v1.1
import unittest
from unittest.mock import patch
from moto import mock_s3, mock_events
import boto3
import json
from handler import create_thumbnail  # replace with your actual module and handler
import time


class TestCreateThumbnail(unittest.TestCase):
    @mock_s3
    @mock_events
    @patch("boto3.client")
    def test_create_thumbnail(self, boto_mock):
        # Create a mock S3 bucket
        s3 = boto3.client("s3", region_name="us-east-1")
        s3.create_bucket(Bucket="photos-yma")
        s3.put_object(
            Bucket="photos-yma", Key="uploads/test_image.jpg", Body=b"test data"
        )

        # Create a mock EventBridge event
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

        # Mock the EventBridge client
        events = boto_mock.return_value
        events.put_events.return_value = {
            "FailedEntryCount": 0,
            "Entries": [{"EventId": "1"}],
        }

        # Call the Lambda handler
        create_thumbnail(event, None)

        # Check that an event was put to EventBridge
        events.put_events.assert_called_once()

        # Check that the thumbnail was created in the S3 bucket
        response = s3.get_object(Bucket="photos-yma", Key="thumbnails/test_image.jpg")
        self.assertEqual(
            response["Body"].read(), b"test thumbnail data"
        )  # replace with your expected thumbnail data


if __name__ == "__main__":
    unittest.main()


@mock_s3
@mock_events
@patch("boto3.client")
def test_create_thumbnail(self, boto_mock):
    # Create a mock S3 bucket
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="photos-yma")

    # Add a delay
    time.sleep(1)

    s3.put_object(Bucket="photos-yma", Key="uploads/test_image.jpg", Body=b"test data")


# Unit Test
@mock_s3
@mock_events
@patch("boto3.client")
def test_create_thumbnail(self, boto_mock):
    # Create a mock S3 bucket
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="photos-yma")

    # Add a delay
    time.sleep(1)

    s3.put_object(Bucket="photos-yma", Key="uploads/test_image.jpg", Body=b"test data")

    # ...
