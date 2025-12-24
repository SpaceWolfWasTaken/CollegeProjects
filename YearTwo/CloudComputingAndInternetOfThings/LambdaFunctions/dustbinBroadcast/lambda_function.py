import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    distance = event['distance']
    client_url = ""
    client = boto3.client("apigatewaymanagementapi", endpoint_url=client_url) 
    
    s3_resource = boto3.resource('s3') # s3
    clients = get_data(s3_resource)
    for id in clients['ids']:
        try:
            client.post_to_connection(Data=json.dumps({"type":"dustbinFill","distance":distance}), ConnectionId=id)
        except:
            remove(s3_resource,id)
    

def get_data(s3_resource):
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

def remove(s3_resource, client_id):
    initial_ids = get_data(s3_resource) #{ids:[]}
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    if client_id in initial_ids['ids']:
        initial_ids['ids'].remove(client_id)
                
        data_string = json.dumps(initial_ids, indent=2, default=str)
        s3_bucket.put_object(
            Key='conns.json',
            Body=data_string
        )