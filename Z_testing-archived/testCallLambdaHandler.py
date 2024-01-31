import unittest
from unittest.mock import patch
from moto import mock_s3, mock_events
import boto3  # if you're using boto3 in your tests
import sys

sys.path.append(
    "/Users/gold/Projects/Assignments/Assignment2/restart-q4-2023-assignment2-amy/Part IV/app/handler.py"
)


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

        # Check the content of the EventBridge event
        call_args = events.put_events.call_args[0]
        self.assertEqual(call_args[0]["Source"], "custom.myApp")
        self.assertEqual(call_args[0]["DetailType"], "ImageProcessing")
        self.assertEqual(json.loads(call_args[0]["Detail"])["status"], "SUCCEEDED")

        # Check that the image was processed and uploaded to S3
        processed_image = s3.get_object(
            Bucket="photos-yma", Key="processed/test_image.jpg"
        )
        self.assertEqual(
            processed_image["Body"].read(), b"test data"
        )  # replace with the expected content of the processed image
