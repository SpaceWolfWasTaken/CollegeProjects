import json

def pay(s3_resource, client_id, amount):
    #overrides to the latest added amount.
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    content = {"type":"payment","id":client_id, "amount":amount}
    # Convert Dictionary to JSON String
    data_string = json.dumps(content, indent=2, default=str)

    s3_bucket.put_object(
        Key='cps.json',
        Body=data_string
    )
    
def get_bal(s3_resource, client_id):
    #overrides to the latest added amount.
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    content = {"type":"getbal","id":client_id}
    # Convert Dictionary to JSON String
    data_string = json.dumps(content, indent=2, default=str)

    s3_bucket.put_object(
        Key='cps.json',
        Body=data_string
    )
    
def update_bal(s3_resource, client_id, amount):
    #overrides to the latest added amount.
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    content = {"type":"updatebal","id":client_id, "amount":amount}
    # Convert Dictionary to JSON String
    data_string = json.dumps(content, indent=2, default=str)

    s3_bucket.put_object(
        Key='cps.json',
        Body=data_string
    )
    
def register(s3_resource, client_id, amount, name, phone):
    #overrides to the latest added amount.
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    content = {"type":"register","id":client_id, "amount":amount, "name":name, "phone":phone}
    # Convert Dictionary to JSON String
    data_string = json.dumps(content, indent=2, default=str)

    s3_bucket.put_object(
        Key='cps.json',
        Body=data_string
    )