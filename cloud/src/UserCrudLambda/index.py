import json
import boto3
from jsonschema import validate
import logging
import os
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import json

# Setup AWS clients
dynamodb = boto3.resource('dynamodb')
sns_client = boto3.client("sns")
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
sns_topic_arn = os.environ["SNS_TOPIC_ARN"]
dynamodb_table_name = os.environ["DYNAMODB_TABLE_NAME"]
table = dynamodb.Table(dynamodb_table_name)

user_info_schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "string"},
        "user_name": {"type": "string"},
        "age": {"type": "string"},
        "address": {"type": "string"}
    },
    "required": ["user_id", "user_name", "age", "address"]
}

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def add_cors(response):
    response["headers"]= {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST, GET, PUT, DELETE",
    }
    return response

def lambda_handler(event,context):
    print(event)
    method = event["httpMethod"]
    if method == "OPTIONS":
        # Handle preflight CORS request
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS, POST, GET, PUT, DELETE",
            },
        }
    elif method == "GET":
        return add_cors(get_user(event))
    elif method == "POST":
        return add_cors(update_user_info(event))
    else:
        return add_cors({"statusCode": 400, "body": json.dumps("Invalid HTTP method")})

def update_user_info(event):
    body = json.loads(event["body"])
    validate(body, user_info_schema)
    
    user_id = body["user_id"]
    update_item(user_id, body)
    send_sns_notification(body)

    return {"statusCode": 200, "body": json.dumps("User information updated successfully")}

def update_item(user_id, body):
    expression = "set " + ", ".join(f"{k}= :{k}" for k in body if k != "user_id")
    expression_values = {f":{k}": body[k] for k in body if k != "user_id"}

    table.update_item(
        Key={"user_id": user_id},
        UpdateExpression=expression,
        ExpressionAttributeValues=expression_values
    )

def get_user(event):
    params = event.get("queryStringParameters", {})
    user_id = None if params is None else params.get("user_id")
    if not user_id:
        result = table.scan()
        users = result.get('Items', {})
    else:
        response = table.get_item(Key={"user_id": user_id})
        users = response.get("Item", {})
    return {
        "statusCode": 200,
        "body": json.dumps(users, cls=DecimalEncoder),
    }

def send_sns_notification(message):
    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=json.dumps({"default": json.dumps(message)}),
        MessageStructure='json'
    )
