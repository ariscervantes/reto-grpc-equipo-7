# Contrato del servicio Reseñas

Guarda las opiniones de los clientes y calcula el promedio de estrellas.

- **Archivo del contrato:** `contratos/resenas.proto`
- **Puerto:** `50053`
- **Paquete:** `tienda.resenas` · **Servicio:** `Resenas`

## Funciones (`rpc`)

| rpc | Tipo | Recibe | Regresa |
|---|---|---|---|
| `PromedioProducto` | unario | `ResenaRequest` | `Promedio` |
| `ListarResenas` | streaming | `ResenaRequest` | muchas `Resena` |

## Reglas del negocio (incluye los errores)

- Un producto **sin reseñas** → `NOT_FOUND` en los dos `rpc`.
- El promedio es `float`: por ejemplo, 3.67 para P003.

## Datos para probar

| Funcionan | Provocan error |
|---|---|
| Claves con reseñas: `P001`, `P002`, `P003`, `P005` | Claves sin reseñas: `P004`, `P006` o `P999` |

## El contrato completo

```proto
syntax = "proto3";

package tienda.resenas;

// Servicio de Reseñas: opiniones de los clientes sobre los productos.
service Resenas {
  // Unario: promedio de estrellas de un producto.
  rpc PromedioProducto (ResenaRequest) returns (Promedio);
  // Streaming: las reseñas de un producto, una por una.
  rpc ListarResenas (ResenaRequest) returns (stream Resena);
}

message ResenaRequest {
  string clave = 1;
}

message Promedio {
  string clave = 1;
  float promedio = 2;
  int32 total = 3;
}

message Resena {
  string autor = 1;
  int32 estrellas = 2;
  string comentario = 3;
}
```
