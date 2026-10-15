# Contrato del servicio Carrito

Guarda lo que cada cliente va a comprar y calcula el total.

- **Archivo del contrato:** `contratos/carrito.proto`
- **Puerto:** `50057`
- **Paquete:** `tienda.carrito` · **Servicio:** `Carrito`

## Funciones (`rpc`)

| rpc | Tipo | Recibe | Regresa |
|---|---|---|---|
| `TotalCarrito` | unario | `CarritoRequest` | `Total` |
| `VerArticulos` | streaming | `CarritoRequest` | muchas `Articulo` |

## Reglas del negocio (incluye los errores)

- Un usuario **sin carrito** → `NOT_FOUND` en los dos `rpc`.
- Los montos van en **centavos**: el total de `ana` es 1329800 ($13,298.00).

## Datos para probar

| Funcionan | Provocan error |
|---|---|
| Usuarios `ana` (2 artículos) y `luis` (3 artículos) | Usuario `pedro` |

## El contrato completo

```proto
syntax = "proto3";

package tienda.carrito;

// Servicio de Carrito: lo que cada cliente lleva en su carrito.
service Carrito {
  // Unario: total a pagar y número de artículos de un cliente.
  rpc TotalCarrito (CarritoRequest) returns (Total);
  // Streaming: los artículos del carrito, uno por uno.
  rpc VerArticulos (CarritoRequest) returns (stream Articulo);
}

message CarritoRequest {
  string usuario = 1;
}

message Total {
  string usuario = 1;
  int32 total_centavos = 2;
  int32 articulos = 3;
}

message Articulo {
  string clave = 1;
  int32 cantidad = 2;
  int32 subtotal_centavos = 3;
}
```
