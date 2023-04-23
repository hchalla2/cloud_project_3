import boto3
import json
from sqs_util import *;
from config import *;

lambda_client = boto3.client('lambda',  aws_access_key_id=get_access_key(), aws_secret_access_key=get_secret_key(), region_name='us-east-1')

while True:

    response = receive_message(get_request_queue_url())

    for message in response.get("Messages", []):
        lambda_parameters = message["Body"]
        
        delete_message(get_request_queue_url(), message['ReceiptHandle']);
        
        lambda_client.invoke(FunctionName='image-function', InvocationType='Event', Payload=lambda_parameters);




        

