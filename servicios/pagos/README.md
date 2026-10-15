# Contrato del servicio Pagos

Sabe qué pedidos están pagados y procesa los cobros paso a paso.

- **Archivo del contrato:** `contratos/pagos.proto`
- **Puerto:** `50056`
- **Paquete:** `tienda.pagos` · **Servicio:** `Pagos`

## Funciones (`rpc`)

| rpc | Tipo | Recibe | Regresa |
|---|---|---|---|
| `ConsultarPago` | unario | `PedidoRequest` | `EstadoPago` |
| `SeguirCobro` | streaming | `CobroRequest` | muchas `PasoCobro` |

## Reglas del negocio (incluye los errores)

- `ConsultarPago` con un pedido que no existe → `NOT_FOUND`.
- `SeguirCobro` con un monto de 0 o negativo → `INVALID_ARGUMENT`.
- `SeguirCobro` manda **3 pasos, uno por segundo**.

## Datos para probar

| Funcionan | Provocan error |
|---|---|
| `ConsultarPago`: `PED-100` (pagado) o `PED-101` (sin pagar)<br>`SeguirCobro`: pedido `PED-101`, monto `89900` | `ConsultarPago`: `PED-999`<br>`SeguirCobro`: monto `0` |

## El contrato completo

```proto
syntax = "proto3";

package tienda.pagos;

// Servicio de Pagos: estado de los pedidos y cobros.
service Pagos {
  // Unario: ¿el pedido ya está pagado y por cuánto?
  rpc ConsultarPago (PedidoRequest) returns (EstadoPago);
  // Streaming: los pasos de un cobro, uno por segundo.
  rpc SeguirCobro (CobroRequest) returns (stream PasoCobro);
}

message PedidoRequest {
  string pedido = 1;
}

message EstadoPago {
  string pedido = 1;
  bool pagado = 2;
  int32 monto_centavos = 3;
}

message CobroRequest {
  string pedido = 1;
  int32 monto_centavos = 2;
}

message PasoCobro {
  int32 numero = 1;
  string paso = 2;
}
```
