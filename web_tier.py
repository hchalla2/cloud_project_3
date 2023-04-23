import boto3
import json
from sqs_util import *;
from config import *;

lambda_client = boto3.client('lambda')

while True:

    response = receive_message(get_request_queue_url())

    for message in response.get("Messages", []):
        message_body = message["Body"]
        message_dict = json.loads(message_body);
        
        delete_message(get_request_queue_url(), message['ReceiptHandle']);
        
        print(message_dict);

        if message_dict.get("Records") != None:
            records = message_dict["Records"]
            for record in records:
                print(record);
                print(record["s3"]["object"])
                video_file_name = record["s3"]["object"]["key"]
                //invoke lambda

                bucket_name = record["s3"]["bucket"]["name"]
                
                lambda_payload = {'bucket_name' : bucket_name, 'file_name' : video_file_name}

                lambda_client.invoke(FunctionName='image-function', InvocationType='Event', Payload=lambda_payload);




        

