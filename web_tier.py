import boto3
import json
from sqs_util import *;
from config import *;

while True:

    response = receive_message(get_request_queue_url())

    for message in response.get("Messages", []):
        message_body = message["Body"]
        message_dict = json.loads(message_body);
        
        
        print(message_dict);
        

