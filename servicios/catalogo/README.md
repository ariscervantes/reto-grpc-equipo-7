# Contrato del servicio Catálogo

Guarda los productos de la tienda: nombre, precio y categoría.

- **Archivo del contrato:** `contratos/catalogo.proto`
- **Puerto:** `50051`
- **Paquete:** `tienda.catalogo` · **Servicio:** `Catalogo`

## Funciones (`rpc`)

| rpc | Tipo | Recibe | Regresa |
|---|---|---|---|
| `ObtenerProducto` | unario | `ProductoRequest` | `Producto` |
| `ListarCategoria` | streaming | `CategoriaRequest` | muchas `Producto` |

## Reglas del negocio (incluye los errores)

- `ObtenerProducto` con una clave que no existe → `NOT_FOUND`.
- `ListarCategoria` con la categoría vacía → `INVALID_ARGUMENT`.
- `ListarCategoria` con una categoría sin productos → `NOT_FOUND`.
- Los precios van en **centavos** (`int32`): 29900 = $299.00.

## Datos para probar

| Funcionan | Provocan error |
|---|---|
| `ObtenerProducto`: clave `P001` … `P006`<br>`ListarCategoria`: `computo`, `audio` o `accesorios` | `ObtenerProducto`: clave `P999`<br>`ListarCategoria`: categoría `""` (vacía) o `juguetes` |

## El contrato completo

```proto
syntax = "proto3";

package tienda.catalogo;

// Servicio de Catálogo: los productos de la tienda.
service Catalogo {
  // Unario: un producto por su clave (por ejemplo "P001").
  rpc ObtenerProducto (ProductoRequest) returns (Producto);
  // Streaming: todos los productos de una categoría, uno por uno.
  rpc ListarCategoria (CategoriaRequest) returns (stream Producto);
}

message ProductoRequest {
  string clave = 1;
}

message CategoriaRequest {
  string categoria = 1;
}

message Producto {
  string clave = 1;
  string nombre = 2;
  int32 precio_centavos = 3;
  string categoria = 4;
}
```
