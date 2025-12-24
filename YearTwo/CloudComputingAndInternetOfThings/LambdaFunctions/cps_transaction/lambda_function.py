import json
import boto3

import get_bal, payments, register, update_bal

def lambda_handler(event, context):
    
    uid = event['UID']
    client_url = ""
    client = boto3.client("apigatewaymanagementapi", endpoint_url=client_url) 
    
    db = boto3.resource("dynamodb")
    table = db.Table("Accounts")
    
    s3_resource = boto3.resource('s3') # s3
    s3_data = get_data(s3_resource)
    
    client_id = s3_data["id"]
    req_type = s3_data["type"]

    match req_type:
        case 'getbal':
            get_bal.get_bal_event(client,s3_resource, client_id, table, uid)
        case 'updatebal':
            amount = s3_data['amount']
            update_bal.update_bal_event(client,s3_resource, client_id, table, uid, amount)
        case 'register':
            name = s3_data['name']
            amount = s3_data['amount']
            phone = s3_data['phone']
            register.register_event(client,s3_resource, client_id, table, uid, name, phone, amount)
        case 'payment':
            amount = s3_data['amount']
            payments.pay_event(client,s3_resource, client_id, table, uid, amount)
        case _:
            client.post_to_connection(Data=json.dumps({"type":"payment","state":0,"body":"This was not supposed to happen."}), ConnectionId=client_id)
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    s3_bucket.put_object(
        Key='cps.json',
        Body=json.dumps({}, indent=2, default=str)
    ) #empty out the file regardless of situation.

    
def get_data(s3_resource):
    s3_object = s3_resource.Object(
            bucket_name='iotdatasc', 
            key='cps.json'
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
