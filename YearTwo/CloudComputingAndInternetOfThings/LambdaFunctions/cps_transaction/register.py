import remove_client
import json

def register(table, uid, name, phone, amount):

    resp = table.get_item(
        Key={
            'UID':uid
        }
    ) #returns a dict with 'Item' if item exists.
    if 'Item' in resp:
        return False #if uid already exists
    else:
        table.put_item(Item={"UID":uid,"Balance":amount,"Name":name,"Phone":phone})
        return True

def register_event(client,s3_resource, client_id, table, uid, name, phone, amount):
    reg = register(table, uid, name, phone, amount)
    try:
        if reg:
            client.post_to_connection(Data=json.dumps({"type":"register","state":1,"body":"Successfully registered."}), ConnectionId=client_id)
            
        else:
            client.post_to_connection(Data=json.dumps({"type":"register","state":0,"body":"UID is already registered."}), ConnectionId=client_id)
    except:
        remove_client.remove(s3_resource,client_id)