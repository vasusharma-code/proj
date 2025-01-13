import json
import boto3
from botocore.exceptions import NoCredentialsError

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    file_content = event.get('file_content')
    file_name = event.get('file_name')
    bucket_name = 'your-s3-bucket-name'
    
    if not file_content or not file_name:
        return {
            'statusCode': 400,
            'body': json.dumps('File content and file name are required.')
        }
    
    try:
       
        file_data = file_content.encode('utf-8')
        
       
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_data,
            ContentType='application/pdf', )
        
       
        file_url = f'https://{bucket_name}.s3.amazonaws.com/{file_name}'
        
        return {
            'statusCode': 200,
            'body': json.dumps({'file_url': file_url})
        }
    
    except NoCredentialsError:
        return {
            'statusCode': 500,
            'body': json.dumps('AWS credentials are not configured correctly.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }
