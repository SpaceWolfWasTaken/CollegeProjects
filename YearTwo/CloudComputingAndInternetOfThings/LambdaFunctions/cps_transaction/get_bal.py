import remove_client
import json

def get_bal(table, uid):

    resp = table.get_item(
        Key={
            'UID':uid
        }
    ) #returns a dict with 'Item' if item exists.
    
    if 'Item' in resp:
        bal = resp['Item']['Balance']
        return bal
    else:
        return 0

def get_bal_event(client,s3_resource, client_id, table, uid):
    bal = get_bal(table, uid)
    try:
        if bal < 0:
            client.post_to_connection(Data=json.dumps({"type":"getbal","state":0,"body":"Card doesn't exist."}), ConnectionId=client_id)
        else:
            client.post_to_connection(Data=json.dumps({"type":"getbal","state":1,"body":str(bal)}), ConnectionId=client_id)
    except:
        remove_client.remove(s3_resource,client_id)
        
