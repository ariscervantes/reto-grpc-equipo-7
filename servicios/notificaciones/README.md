# Contrato del servicio Notificaciones

Manda avisos a los clientes y les entrega los que tienen pendientes.

- **Archivo del contrato:** `contratos/notificaciones.proto`
- **Puerto:** `50054`
- **Paquete:** `tienda.notificaciones` · **Servicio:** `Notificaciones`

## Funciones (`rpc`)

| rpc | Tipo | Recibe | Regresa |
|---|---|---|---|
| `EnviarAviso` | unario | `Aviso` | `Confirmacion` |
| `Suscribirse` | streaming | `Suscripcion` | muchas `Aviso` |

## Reglas del negocio (incluye los errores)

- `EnviarAviso` con el destinatario o el mensaje vacíos → `INVALID_ARGUMENT`.
- `Suscribirse` de alguien sin avisos → `NOT_FOUND`.
- Un aviso enviado con `EnviarAviso` aparece después en `Suscribirse` de ese destinatario.

## Datos para probar

| Funcionan | Provocan error |
|---|---|
| `EnviarAviso`: destinatario `ana`, mensaje `Hola`<br>`Suscribirse`: `ana` (3 avisos) o `luis` (1) | `EnviarAviso`: mensaje `""` (vacío)<br>`Suscribirse`: `pedro` |

## El contrato completo

```proto
syntax = "proto3";

package tienda.notificaciones;

// Servicio de Notificaciones: avisos para los clientes.
service Notificaciones {
  // Unario: registra un aviso nuevo para un cliente.
  rpc EnviarAviso (Aviso) returns (Confirmacion);
  // Streaming: entrega, uno por uno, los avisos pendientes de un cliente.
  rpc Suscribirse (Suscripcion) returns (stream Aviso);
}

message Aviso {
  string destinatario = 1;
  string mensaje = 2;
}

message Confirmacion {
  string folio = 1;
  bool entregado = 2;
}

message Suscripcion {
  string destinatario = 1;
}
```
