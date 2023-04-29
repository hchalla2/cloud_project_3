import os
import boto3
import json
from sqs_util import *;
from config import *;

temp_dir = "";
s3 = boto3.client('s3', aws_access_key_id=get_access_key(), aws_secret_access_key=get_secret_key(), region_name='us-east-1')

"""
    This function deletes file from disk of app instance.
"""
def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

while True:

    response = receive_message(get_response_queue_url())

    for message in response.get("Messages", []):
        message_body = message["Body"]
        message_dict = json.loads(message_body);
        
        delete_message(get_response_queue_url(), message['ReceiptHandle']);
        
        for record in message_dict.get("Records", []):
            results_file_name = record["s3"]["object"]["key"]
            bucket_name = record["s3"]["bucket"]["name"]
    
            results_path = temp_dir + results_file_name
            with open(results_path, 'wb') as results_file:
                    s3.download_fileobj(bucket_name, results_file_name, results_file)


            with open(results_path, 'r') as results_file:
                results = results_file.read();
                print(f'{results_file_name} : {results}')    

            remove_file(results_path);
        

