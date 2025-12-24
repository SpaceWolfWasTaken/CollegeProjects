import json
import boto3
import base64

def lambda_handler(event, context):
    
    s3_resource = boto3.resource('s3') # s3
    
    add_image(s3_resource,event['image'])
    
    #code to send labels to all connected clients.
    client_url = ""
    client = boto3.client("apigatewaymanagementapi", endpoint_url=client_url) 
    ids = get_conns(s3_resource)
    labels_ = json.dumps(labels('iotdatasc','testimg.jpg'))
    for id in ids["ids"]:
        client.post_to_connection(Data=labels_, ConnectionId=id)
    
    return {
        'statusCode': 200
    }


def add_image(s3_resource, img_buffer):
    #get img as b64 buffer. decode to paste.
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    
    s3_bucket.put_object(
        Key='testimg.jpg',
        Body=base64.b64decode(img_buffer)
    )
    
def get_image(s3_resource):
    s3_object = s3_resource.Object(
            bucket_name='iotdatasc', 
            key='testimg.jpg'
        )
        
    content = s3_object.get().get('Body')
    decoded = base64.b64encode(content.read()).decode() #since this is base-64 encoded, user has to b64decode to use data.
    return decoded
    
    
def labels(bucket_name, image_key):
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
    return response['Labels']
    
def get_conns(s3_resource):
    s3_object = s3_resource.Object(
            bucket_name='iotdatasc', 
            key='conns.json'
        )
    # Get the response from get_object()
    s3_response = s3_object.get()
    
    # Get the Body object in the S3 get_object() response
    s3_object_body = s3_response.get('Body')
    
    # Read the data in bytes format
    content = s3_object_body.read()

    # Parse JSON content to Python Dictionary
    json_dict = json.loads(content)
    
    return json_dict