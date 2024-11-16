# lambda_functions/listarMovimientos.py
import boto3
import json

# {
#     usuario_id: string	
# }

dynamodb = boto3.resource('dynamodb')
movimientos_table = dynamodb.Table('TABLA-MOVIMIENTOS')

def lambda_handler(event, context):
    usuario_id = event['queryStringParameters']['usuario_id']
    
    response = movimientos_table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('usuario_id').eq(usuario_id)
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response.get('Items', []))
    }
