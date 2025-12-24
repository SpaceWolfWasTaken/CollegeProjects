import json
import boto3

bucket_name = 'iotdatasc'
image_key = 'testimg.jpg'

def lambda_handler(event, context):
    rekognition_client = boto3.client('rekognition')

    # Call DetectLabels API
    response = rekognition_client.detect_labels(
       Image={
            'S3Object': {
               'Bucket': bucket_name,
               'Name': image_key
           }
       }
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response['Labels'])
    }
