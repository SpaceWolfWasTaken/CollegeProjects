import remove_client
import json
import boto3
def pay(table, uid, amount):

    resp = table.get_item(
        Key={
            'UID':uid
        }
    ) #returns a dict with 'Item' if item exists.
    if 'Item' in resp:
        item = resp['Item']
        bal = item['Balance']
        if bal <= amount:
            return False #if amount is greater than bal
        bal = bal - amount
        table.put_item(Item={"UID":item['UID'],"Balance":bal,"Name":item['Name'],"Phone":item['Phone']})
        phones = []
        if str(item['Phone']) in phones:
            msg = f"Your card {item['UID']} has been deducted by {amount}."
            sns = boto3.client('sns')
            number = '+977'+str(item['Phone'])
            response = sns.publish(PhoneNumber=number,Message=msg)
        return True
    else:
        return False #if uid doesn't exist

def pay_event(client,s3_resource, client_id, table, uid, amount):
    bal = pay(table, uid, amount)
    try:
        if bal:
            client.post_to_connection(Data=json.dumps({"type":"payment","state":1,"body":"Successfully paid."}), ConnectionId=client_id)
            
        else:
            client.post_to_connection(Data=json.dumps({"type":"payment","state":0,"body":"Failed to pay."}), ConnectionId=client_id)
    except:
        remove_client.remove(s3_resource,client_id)