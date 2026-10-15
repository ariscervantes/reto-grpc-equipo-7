# Reto de integración · Tienda en línea con gRPC

Programación Distribuida · Unidad II · Facultad de Telemática, Universidad de Colima

Cada equipo es **un servicio** de la tienda. Hacen **dos programas**:

1. **El servidor de su servicio**, tal como lo pide su contrato (`.proto`).
2. **Un cliente que usa el servicio del equipo vecino**, leyendo solo su contrato y su README.

Lo que esté en GitHub **a las 8:55** es lo que se califica.

## Los servicios

| Servicio | Nombre para los comandos | Puerto |
|---|---|---|
| Catálogo | `catalogo` | 50051 |
| Inventario | `inventario` | 50052 |
| Reseñas | `resenas` | 50053 |
| Notificaciones | `notificaciones` | 50054 |
| Envíos | `envios` | 50055 |
| Pagos | `pagos` | 50056 |
| Carrito | `carrito` | 50057 |

El contrato de cada uno, con sus reglas y los datos para probar, está en `servicios/<servicio>/README.md`.

## Paso a paso

**1. Crea el repositorio de tu equipo (una sola persona):** en esta página, **Use this template → Create a new repository**, como **Public**. Agrega a tus compañeros: **Settings → Collaborators**.

**2. Ábrelo en tu Codespace:** **Code → Codespaces → Create codespace on main**.

**3. Prepáralo con tu servicio y el de tu vecino** (te los da el profesor en el sorteo):

```bash
python preparar.py <tu_servicio> <servicio_vecino>
bash compilar.sh
```

**4. Terminal 1 · Su servidor.** Completen los `TODO` de `servidor.py` y córranlo:

```bash
python servidor.py
```

Cada cambio al servidor: **Ctrl+C** y vuelvan a correrlo.

**5. Terminal 2 · El servidor del vecino.** Clonen su repositorio en una carpeta aparte y córranlo **sin modificarlo**:

```bash
git clone https://github.com/USUARIO/REPO-DEL-VECINO ../vecino
cd ../vecino
bash compilar.sh
python servidor.py
```

**6. Terminal 3 · Su cliente.** Completen los `TODO` de `cliente_vecino.py` y córranlo:

```bash
python cliente_vecino.py
```

**7. Commit y push** (lo hace quien escribió el código, para que quede su nombre):

```bash
git add .
git commit -m "Servidor: ObtenerProducto con NOT_FOUND"
git push
```

**8. Prueba cruzada (8:30–8:50).** Corran su cliente contra el servidor **real** del vecino y peguen la salida en `EQUIPO.md`, junto con los enlaces a sus *issues* y su declaración de uso de IA. Hagan commit y push antes de las **8:55**.

## El martes 20

Cada equipo saca una **tarjeta de cambio** (un cambio pequeño a su servicio o a su cliente) y tiene 15 minutos para hacerlo. Luego corren su integración frente al grupo y **cada integrante** contesta una pregunta sobre el código del equipo. Lleguen con el Codespace abierto y los dos servidores listos para correr.

## Reglas

- **No modifiquen el contrato** (`.proto`). Si algo del contrato del vecino no se entiende, abran un **issue** en el repositorio del vecino; ellos contestan ahí.
- **Pueden usar IA.** Declárenlo en `EQUIPO.md`, de acuerdo con el Acuerdo No. 23/2024 UdeC. Cualquier integrante debe poder explicar cualquier línea: el profesor pregunta a quien sea.
- **Cada integrante hace sus commits** con su cuenta. El historial de GitHub muestra quién hizo qué.
- Llenen `EQUIPO.md` con integrantes, roles y la URL del repositorio del vecino.

## Errores que pueden salir

| Mensaje | Qué significa |
|---|---|
| `No hay contratos en esta carpeta` | Falta `python preparar.py ...`. |
| `ModuleNotFoundError: No module named '..._pb2'` | Falta `bash compilar.sh`. |
| `StatusCode.UNIMPLEMENTED` `Falta implementar ...` | Ese `rpc` todavía tiene su `TODO` en el servidor, o el servidor que corre es el viejo (Ctrl+C y volver a correrlo). |
| `StatusCode.UNAVAILABLE ... Connection refused` | El servidor del vecino no está corriendo o el puerto no coincide. |
| `AttributeError: '_MultiThreadedRendezvous' object has no attribute ...` | Usaron la respuesta de streaming sin `for`. |
| `StatusCode.UNKNOWN ... 'X' object is not an iterator` | En un `rpc` de streaming usaron `return` en lugar de `yield`. |
| `git clone ... Repository not found` | El repositorio del vecino no es público o la URL está mal. |
