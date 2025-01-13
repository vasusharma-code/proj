import json

def lambda_handler(event, context):

    num1 = event.get('num1')
    num2 = event.get('num2')
    
   
    if num1 is None or num2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Both numbers must be provided in the event.')
        }
    
   
    result = num1 + num2
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'The result is: {result}')
    }
