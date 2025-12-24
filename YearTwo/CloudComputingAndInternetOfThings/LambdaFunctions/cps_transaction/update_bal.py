import remove_client
import json
import boto3
def update_bal(table, uid, amount):

    resp = table.get_item(
        Key={
            'UID':uid
        }
    ) #returns a dict with 'Item' if item exists.
    if 'Item' in resp:
        item = resp['Item']
        bal = item['Balance']
        
        bal = bal + amount
        table.put_item(Item={"UID":item['UID'],"Balance":bal,"Name":item['Name'],"Phone":item['Phone']})
        phones = []
        if str(item['Phone']) in phones:
            msg = f"Your card {item['UID']} has been credited by {amount}."
            sns = boto3.client('sns')
            number = '+977'+str(item['Phone'])
            response = sns.publish(PhoneNumber=number,Message=msg)
        return True
    else:
        return False

def update_bal_event(client,s3_resource, client_id, table, uid, amount):
    bal = update_bal(table, uid, amount)
    try:
        if bal:
            client.post_to_connection(Data=json.dumps({"type":"updatebal","state":1,"body":"Updated balance."}), ConnectionId=client_id)
            #call SNS
        else:
            client.post_to_connection(Data=json.dumps({"type":"updatebal","state":0,"body":"Failed to update balance."}), ConnectionId=client_id)
    except:
        remove_client.remove(s3_resource,client_id)