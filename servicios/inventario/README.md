# Contrato del servicio Inventario

Sabe cuántas piezas hay de cada producto y en qué almacén están.

- **Archivo del contrato:** `contratos/inventario.proto`
- **Puerto:** `50052`
- **Paquete:** `tienda.inventario` · **Servicio:** `Inventario`

## Funciones (`rpc`)

| rpc | Tipo | Recibe | Regresa |
|---|---|---|---|
| `ConsultarExistencia` | unario | `ExistenciaRequest` | `Existencia` |
| `VigilarExistencia` | streaming | `ExistenciaRequest` | muchas `Existencia` |

## Reglas del negocio (incluye los errores)

- `ConsultarExistencia` y `VigilarExistencia` con una clave que no existe → `NOT_FOUND`.
- `VigilarExistencia` manda **4 actualizaciones, una por segundo**; en cada una la cantidad baja 1 (nunca menos de 0).
- Que la cantidad sea 0 **no es error**: significa que se agotó.

## Datos para probar

| Funcionan | Provocan error |
|---|---|
| Claves `P001` … `P006` (la `P004` tiene 0 piezas) | Clave `P999` |

## El contrato completo

```proto
syntax = "proto3";

package tienda.inventario;

// Servicio de Inventario: existencias por producto.
service Inventario {
  // Unario: cuántas piezas hay de un producto.
  rpc ConsultarExistencia (ExistenciaRequest) returns (Existencia);
  // Streaming: la existencia de un producto mientras se vende (4 actualizaciones).
  rpc VigilarExistencia (ExistenciaRequest) returns (stream Existencia);
}

message ExistenciaRequest {
  string clave = 1;
}

message Existencia {
  string clave = 1;
  int32 cantidad = 2;
  string almacen = 3;
}
```
