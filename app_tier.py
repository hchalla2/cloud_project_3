import boto3
import json
from sqs_util import *;
from config import *;

temp_dir = "";

while True:

    response = receive_message(get_response_queue_url())

    for message in response.get("Messages", []):
        message_body = message["Body"]
        message_dict = json.loads(message_body);
        
        delete_message(get_response_queue_url(), message['ReceiptHandle']);
        
        print(message_dict);

        if message_dict.get("Records") != None:
            records = message_dict["Records"]
            for record in records:
                print(record);
                print(record["s3"]["object"])
                results_file_name = record["s3"]["object"]["key"]
                bucket_name = record["s3"]["bucket"]["name"]
    
                //invoke lambda
                results_path = temp_dir + results_file_name
                with open(results_path, 'wb') as results_file:
                     s3.download_fileobj(bucket_name, results_file_name, results_file)


                with open(results_path, 'r') as results_file:
                    results = results_file.read();
                    print(f'{results_file_name} : {results}')    


        

