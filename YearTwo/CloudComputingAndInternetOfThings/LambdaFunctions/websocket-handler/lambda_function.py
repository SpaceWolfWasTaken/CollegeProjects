import json
import boto3

import s3_conns, imgs, transactions

def lambda_handler(event, context):
    
    client_url = ""
    client = boto3.client("apigatewaymanagementapi", endpoint_url=client_url) 
    
    s3_resource = boto3.resource('s3') # s3
    
    conn_id = event.get("requestContext", {}).get("connectionId")
    route_key = event.get("requestContext", {}).get("routeKey")
    match route_key:
        case '$connect':
            s3_conns.make_empty(s3_resource,'conns.json') #just to make the json first time # testing for only one client. make sure to remove in prod
            initial_ids = s3_conns.get_data(s3_resource,'conns.json') #{ids:[]}
            if conn_id not in initial_ids['ids']:
                s3_conns.add_conn(s3_resource,initial_ids,conn_id)
        case '$disconnect':
            initial_ids = s3_conns.get_data(s3_resource,'conns.json') #{ids:[]}
            if conn_id in initial_ids['ids']:
                s3_conns.remove_conn(s3_resource,initial_ids,conn_id)
        case '$default':
            pass
        case 'echo':
            body = event['body']#.get("body", {})
            echo(client, conn_id, body)
        case 'dustbinFill':
            ids = s3_conns.get_data(s3_resource,'conns.json')
            for id in ids["ids"]:
                echo(client, id, json.dumps(ids))
        case 'parkingSpots':
            #img = event['image']
            #imgs.add_image(s3_resource,img)
            pass
        case 'transaction':
            
            #s3_conns.make_empty(s3_resource,'cps.json')
            event_body = json.loads(event['body']) #gets event body
            event_body = event_body['body'] #gets the body key within event body
            req_type = "" 
            try:
                req_type = event_body['type'] #the type of request
            except:
                req_type = "X"
            req = True
            
            match req_type:
                case 'getbal':
                    transactions.get_bal(s3_resource,conn_id)
                case 'updatebal':
                    amount = event_body['amount']
                    transactions.update_bal(s3_resource, conn_id, amount)
                case 'register':
                    name = event_body['name']
                    amount = event_body['amount']
                    phone = event_body['phone']
                    transactions.register(s3_resource, conn_id, amount, name, phone)
                case 'payment':
                    amount = event_body['amount']
                    transactions.pay(s3_resource,conn_id,amount)
                case _:
                    echo(client,conn_id,json.dumps({"type":"transaction", "state": 0, "body":"Error"}))
                    req = False
            if req:
                echo(client,conn_id,json.dumps({"type":"transaction", "state": 1, "body":"Successfully added."}))
    return {
        'statusCode': 200
    }
    

def echo(client, id, body):
    #json.dumps(body) no need when grabbing from event['body']
    client.post_to_connection(Data=body, ConnectionId=id)
    
