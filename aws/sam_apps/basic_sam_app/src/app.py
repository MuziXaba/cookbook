import json, os
import boto3

print("loading function")
region_name = os.environ['REGION_NAME']
dynamo = boto3.client('dynamodb', region_name=region_name)
table_name = os.environ['TABLE_NAME']

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
def lambda_handler(event, context):
    """My first SAM built lambda"""
    print("Event received: " + json.dumps(event, indent=2))
    scan_res = dynamo.scan(TableName=table_name)
    return respond(None, res=scan_res)