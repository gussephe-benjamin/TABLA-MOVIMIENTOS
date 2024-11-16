# lambda_functions/registrarMovimiento.py
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
movimientos_table = dynamodb.Table('TABLA-MOVIMIENTOS')

def lambda_handler(event, context):
    for record in event['Records']:
        # Extraer el ARN de la tabla que generó el evento
        event_source_arn = record['eventSourceARN']
        new_image = record['dynamodb'].get('NewImage', {})

        # Obtener información básica del movimiento
        usuario_id = new_image.get('usuario_id', {}).get('S', 'usuario_desconocido')
        monto = int(new_image.get('monto', {}).get('N', 0))
        cuenta_origen = new_image.get('cuenta_origen', {}).get('S', 'sin_cuenta')
        cuenta_destino = new_image.get('cuenta_destino', {}).get('S', 'sin_cuenta')
        resultado = new_image.get('resultado', {}).get('S', 'desconocido')

        # Determinar el tipo de movimiento y ajustar el monto según la operación
        if 'TABLA-TRANSACCION' in event_source_arn:
            tipo_movimiento = 'transaccion'
            descripcion = "Transacción exitosa" if resultado == 'exitoso' else "Transacción fallida"
            # Si es una salida de dinero de la cuenta de origen, registra como monto negativo
            if resultado == 'exitoso':
                monto = -monto  # Registramos como salida de dinero (negativo) para transacciones exitosas

        elif 'TABLA-PAGOS' in event_source_arn:
            tipo_movimiento = 'pago'
            descripcion = "Pago realizado" if resultado == 'exitoso' else "Pago fallido"
            # Pagos exitosos son salidas de dinero, así que registramos monto negativo
            if resultado == 'exitoso':
                monto = -monto

        elif 'TABLA-PRESTAMOS' in event_source_arn:
            tipo_movimiento = 'prestamo'
            descripcion = "Préstamo aceptado" if resultado == 'exitoso' else "Préstamo rechazado"
            # Préstamos aceptados son entradas de dinero, monto positivo
            if resultado == 'exitoso':
                monto = abs(monto)  # Aseguramos que sea positivo

        elif 'TABLA-SOLICITUDES' in event_source_arn:
            tipo_movimiento = 'solicitud'
            descripcion = "Solicitud creada"
            # Las solicitudes pueden no tener un impacto directo en el monto, así que lo dejamos como está

        # Insertar el movimiento en la tabla de Movimientos
        movimientos_table.put_item(
            Item={
                'usuario_id': usuario_id,
                'fecha_movimiento': datetime.utcnow().isoformat(),
                'tipo_movimiento': tipo_movimiento,
                'monto': monto,
                'cuenta_origen': cuenta_origen,
                'cuenta_destino': cuenta_destino,
                'descripcion': descripcion
            }
        )
        
    return {'statusCode': 200, 'body': 'Movimientos registrados'}
