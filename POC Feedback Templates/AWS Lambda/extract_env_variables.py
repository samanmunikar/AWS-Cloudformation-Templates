import os

def lambda_handler(event, context):
    return os.getenv('MY_ENV_VAR')
