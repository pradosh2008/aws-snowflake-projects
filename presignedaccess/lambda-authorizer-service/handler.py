import json

def authenticate_user(event, context):
    body = {
        "message": "User authenticated successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
