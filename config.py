access_key = 'A';
secret_key = 'S'
request_queue_url = 'https://sqs.us-east-1.amazonaws.com/798194651907/event-sqs-queue';
response_queue_url = 'https://sqs.us-east-1.amazonaws.com/798194651907/response_queue-hsh';

def get_access_key():
    return access_key;

def get_secret_key():
    return secret_key;

def get_request_queue_url():
    return request_queue_url;

def get_response_queue_url():
    return response_queue_url;

