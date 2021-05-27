import boto3
import os

def new_client(resource):
    return boto3.client(resource)

def sanitize(key_name):
    v = os.environ.get(f"INPUT_{key_name}")
    if not v:
        raise Exception(f"Unable to find the {key_name}. Did you set {key_name}?")
    return v

def set_aws_env(key_id, key_secret, region):
    os.environ['AWS_ACCESS_KEY_ID'] = key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = key_secret
    os.environ['AWS_DEFAULT_REGION'] = region

def check_lambda_exists(client, function_name):
    try:
        if client.get_function(FunctionName=function_name):
            return True
    except client.exceptions.ResourceNotFoundException:
        return False

def create_function(client, aws_account_id, function_name, role_name, image_uri):
    print("NOW CREATING A LAMBDA FUNCTION")
    try:
        response = client.create_function(
            FunctionName=function_name,
            PackageType="Image",
            Role=f"arn:aws:iam::{aws_account_id}:role/{role_name}", #this is formatted as the ARN of the lambda's role 
            Code={
                'ImageUri': image_uri,
            },
        )
        print("FINISHED SUCCESSFULLY CREATING A LAMBDA FUNCTION")
        return response
    except Exception as e:
        print(e)
        exit(1)

def update_function():
    print("updating function code")

def main():
    aws_account_id = sanitize("AWS_ACCOUNT_ID")
    access_key_id = sanitize("ACCESS_KEY_ID")
    secret_access_key = sanitize("SECRET_ACCESS_KEY")
    region = sanitize("REGION")
    function_name = sanitize("FUNCTION_NAME")
    role_name = sanitize("ROLE_NAME")
    image_uri = sanitize("IMAGE_URI")

    set_aws_env(access_key_id, secret_access_key, region)
    lambda_client = new_client('lambda')

    if not check_lambda_exists(lambda_client, function_name):
        print(create_function(
            lambda_client,
            aws_account_id, 
            function_name, 
            role_name, 
            image_uri     
        ))
    else:
        update_function()


main()
