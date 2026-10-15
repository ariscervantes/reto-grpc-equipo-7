# Contrato del servicio Envíos

Cotiza cuánto cuesta un envío y rastrea los paquetes.

- **Archivo del contrato:** `contratos/envios.proto`
- **Puerto:** `50055`
- **Paquete:** `tienda.envios` · **Servicio:** `Envios`

## Funciones (`rpc`)

| rpc | Tipo | Recibe | Regresa |
|---|---|---|---|
| `CotizarEnvio` | unario | `CotizacionRequest` | `Cotizacion` |
| `Rastrear` | streaming | `GuiaRequest` | muchas `EstadoEnvio` |

## Reglas del negocio (incluye los errores)

- `CotizarEnvio` con un código postal que no sea de 5 dígitos, o con peso 0 o negativo → `INVALID_ARGUMENT`.
- Costo = 9900 + 2000 por cada kilo completo. Días = 1 para códigos de Colima (empiezan con 28); 3 para los demás.
- `Rastrear` con una guía que no existe → `NOT_FOUND`.

## Datos para probar

| Funcionan | Provocan error |
|---|---|
| `CotizarEnvio`: CP `28000`, 2500 g → 13900 centavos, 1 día<br>`Rastrear`: `GUIA-500` (4 estados) o `GUIA-501` (2) | `CotizarEnvio`: CP `280` o peso `0`<br>`Rastrear`: `GUIA-999` |

## El contrato completo

```proto
syntax = "proto3";

package tienda.envios;

// Servicio de Envíos: cotización y rastreo de paquetes.
service Envios {
  // Unario: costo y días de entrega para un código postal y un peso.
  rpc CotizarEnvio (CotizacionRequest) returns (Cotizacion);
  // Streaming: los estados de un paquete, uno por segundo.
  rpc Rastrear (GuiaRequest) returns (stream EstadoEnvio);
}

message CotizacionRequest {
  string codigo_postal = 1;
  int32 peso_gramos = 2;
}

message Cotizacion {
  int32 costo_centavos = 1;
  int32 dias = 2;
}

message GuiaRequest {
  string guia = 1;
}

message EstadoEnvio {
  string guia = 1;
  string estado = 2;
  string lugar = 3;
}
```
