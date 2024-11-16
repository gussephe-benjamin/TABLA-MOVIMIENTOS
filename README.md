# TABLA-MOVIMIENTOS

Aquí tienes los JSON de entrada para las operaciones relacionadas con la tabla **Movimientos**:

---

### **1. Registrar Movimiento** (Usado internamente por Streams)
**Este proceso es automático y no requiere un JSON de entrada directo del usuario. Sin embargo, así sería un ejemplo del JSON que se registra:**

```json
{
    "usuario_id": "CLIENTE-14",
    "fecha_movimiento": "2024-11-16T12:30:00.000Z",
    "tipo_movimiento": "transaccion",
    "monto": 150.00,
    "cuenta_origen": "CUENTA-ORIGEN-123",
    "cuenta_destino": "CUENTA-DESTINO-456",
    "descripcion": "Transferencia realizada con éxito"
}
```

---

### **2. Listar Movimientos**
**Endpoint: GET `/movimientos`**

**Entrada JSON:**
```json
{
    "usuario_id": "CLIENTE-14"
}
```

**Salida esperada:**
```json
[
    {
        "usuario_id": "CLIENTE-14",
        "fecha_movimiento": "2024-11-15T09:15:00.000Z",
        "tipo_movimiento": "pago",
        "monto": -200.00,
        "descripcion": "Pago realizado para servicio eléctrico"
    },
    {
        "usuario_id": "CLIENTE-14",
        "fecha_movimiento": "2024-11-14T10:00:00.000Z",
        "tipo_movimiento": "prestamo",
        "monto": 5000.00,
        "descripcion": "Préstamo aceptado y acreditado"
    }
]
```

---

### **3. Obtener Movimiento**
**Endpoint: GET `/movimientos/detalle`**

**Entrada JSON:**
```json
{
    "usuario_id": "CLIENTE-14",
    "fecha_movimiento": "2024-11-15T09:15:00.000Z"
}
```

**Salida esperada:**
```json
{
    "usuario_id": "CLIENTE-14",
    "fecha_movimiento": "2024-11-15T09:15:00.000Z",
    "tipo_movimiento": "pago",
    "monto": -200.00,
    "descripcion": "Pago realizado para servicio eléctrico"
}
```

---

### **4. Eliminar Movimiento**
**Endpoint: DELETE `/movimientos/eliminar`**

**Entrada JSON:**
```json
{
    "usuario_id": "CLIENTE-14",
    "fecha_movimiento": "2024-11-15T09:15:00.000Z"
}
```

**Salida esperada:**
```json
{
    "mensaje": "Movimiento con fecha 2024-11-15T09:15:00.000Z del usuario CLIENTE-14 fue eliminado con éxito"
}
```

---

Estos JSON cubren las operaciones principales relacionadas con la tabla de movimientos. Si necesitas ajustar algo o agregar más detalles, ¡házmelo saber!
