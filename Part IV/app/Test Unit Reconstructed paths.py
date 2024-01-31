# Unit Test Reconstructed paths using bucket name
"""
Based on the information provided, it's possible the S3 event record's key field could already include the uploads/ or thumbnails/ prefix if those are set as the object key.
- To avoid potentially having duplicate prefixes like "uploads/uploads/" in the paths, modifications have been made to:
- (1) Extract just the filename from the key, removing any prefixes: `filename = original_s3_path.split('/')[-1]` And 
- (2) Reconstructed the paths using the bucket name and prefixes directly rather than with the key: 
- `original_s3_path = f"s3://{bucket_name}/uploads/{filename}`
- `destination_s3_path = f"s3://{bucket_name}/thumbnails/{filename}"` 
- (3) Changed Download and process using the filename only to make sure the paths always have the expected prefix structure without relying on what is included in the event key. 
- s3://photos-yma/uploads/
- arn:aws:s3:::photos-yma/uploads/
- s3://photos-yma/thumbnails/	
- arn:aws:s3:::photos-yma/thumbnails/
"""
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
                    "object": {"key": "test_image.jpg"},
                }
            }
        ]
    }

    # Call the function with the mock event
    create_thumbnail(event, None)

    # Check that the thumbnail was created
    assert conn.Object("mybucket", "thumbnails/test_image.jpg").get()


test_create_thumbnail()
def create_thumbnail(event, context):
    try:
        for record in event["Records"]:
            bucket_name = record["s3"]["bucket"]["name"]
            original_s3_path = unquote_plus(record["s3"]["object"]["key"])
            # ...

            # After the thumbnail is created, send an event to EventBridge
            events_client.put_events(
                Entries=[
                    {
                        "Source": "custom.myApp",
                        "DetailType": "thumbnailCreated",
                        "Detail": json.dumps(
                            {
                                "bucket": bucket_name,
                                "thumbnailPath": destination_s3_path,
                            }
                        ),
                        "EventBusName": "supercalifragilisticexpialidocious-eventbus",
                    }
                ]
            )
    except Exception as ex:
        print("Error processing image: ", ex)
        raise
