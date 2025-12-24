import json

def add_conn(s3_resource, initial_ids, id):
    
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    initial_ids['ids'].append(id)
    # Convert Dictionary to JSON String
    data_string = json.dumps(initial_ids, indent=2, default=str)

    s3_bucket.put_object(
        Key='conns.json',
        Body=data_string
    )
    
def get_data(s3_resource, name):
    s3_object = s3_resource.Object(
            bucket_name='iotdatasc', 
            key=name
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
    
def remove_conn(s3_resource, initial_ids, id):
    
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    initial_ids['ids'].remove(id)

    # Convert Dictionary to JSON String
    data_string = json.dumps(initial_ids, indent=2, default=str)

    s3_bucket.put_object(
        Key='conns.json',
        Body=data_string
    )
    
def make_empty(s3_resource, name):
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    
    initial_ids = {"ids":[]}
    # Convert Dictionary to JSON String
    data_string = json.dumps(initial_ids, indent=2, default=str)

    s3_bucket.put_object(
        Key=name,
        Body=data_string
    )