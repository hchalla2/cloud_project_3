import boto3
import json
from sqs_util import *;
from config import *;

while True:

    response = receive_message(get_request_queue_url())

    for message in response.get("Messages", []):
        message_body = message["Body"]
        message_dict = json.loads(message_body);
        
        delete_message(get_request_queue_url(), message['ReceiptHandle']);
        
        print(message_dict);

        records = message_dict['Records']
        for record in records:
            print(record['object'])
        
