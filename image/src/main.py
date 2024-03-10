import json
import requests

def handler(event, context):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        users = response.json()
        
        return {
            'statusCode': 200,
            'body': json.dumps(users)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
