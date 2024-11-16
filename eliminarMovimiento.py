# lambda_functions/eliminarMovimiento.py
import boto3
import json

dynamodb = boto3.resource('dynamodb')
movimientos_table = dynamodb.Table('TABLA-MOVIMIENTOS')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    usuario_id = data['usuario_id']
    fecha_movimiento = data['fecha_movimiento']
    
    response = movimientos_table.delete_item(
        Key={
            'usuario_id': usuario_id,
            'fecha_movimiento': fecha_movimiento
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Movimiento {fecha_movimiento} eliminado exitosamente'})
    }
