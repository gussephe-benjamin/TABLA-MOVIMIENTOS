# lambda_functions/obtenerMovimiento.py
import boto3
import json

dynamodb = boto3.resource('dynamodb')
movimientos_table = dynamodb.Table('TABLA-MOVIMIENTOS')

def lambda_handler(event, context):
    data = event['queryStringParameters']
    usuario_id = data['usuario_id']
    fecha_movimiento = data['fecha_movimiento']
    
    response = movimientos_table.get_item(
        Key={
            'usuario_id': usuario_id,
            'fecha_movimiento': fecha_movimiento
        }
    )
    
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Movimiento no encontrado'})
        }
