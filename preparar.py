# Prepara tu repositorio para el reto: copia tu contrato, el del equipo vecino,
# el esqueleto de tu servidor y el de tu cliente.
# Uso:  python preparar.py <tu_servicio> <servicio_vecino>
# Ejemplo: python preparar.py carrito catalogo
import os, shutil, sys

SERVICIOS = {
  "catalogo": {
    "nombre": "Catálogo",
    "clase": "Catalogo",
    "puerto": 50051,
    "unario": "ObtenerProducto",
    "stream": "ListarCategoria"
  },
  "inventario": {
    "nombre": "Inventario",
    "clase": "Inventario",
    "puerto": 50052,
    "unario": "ConsultarExistencia",
    "stream": "VigilarExistencia"
  },
  "resenas": {
    "nombre": "Reseñas",
    "clase": "Resenas",
    "puerto": 50053,
    "unario": "PromedioProducto",
    "stream": "ListarResenas"
  },
  "notificaciones": {
    "nombre": "Notificaciones",
    "clase": "Notificaciones",
    "puerto": 50054,
    "unario": "EnviarAviso",
    "stream": "Suscribirse"
  },
  "envios": {
    "nombre": "Envíos",
    "clase": "Envios",
    "puerto": 50055,
    "unario": "CotizarEnvio",
    "stream": "Rastrear"
  },
  "pagos": {
    "nombre": "Pagos",
    "clase": "Pagos",
    "puerto": 50056,
    "unario": "ConsultarPago",
    "stream": "SeguirCobro"
  },
  "carrito": {
    "nombre": "Carrito",
    "clase": "Carrito",
    "puerto": 50057,
    "unario": "TotalCarrito",
    "stream": "VerArticulos"
  }
}

def salir(msg):
    print(msg); sys.exit(1)

if len(sys.argv) != 3:
    salir("Uso: python preparar.py <tu_servicio> <servicio_vecino>\nServicios: " + ", ".join(SERVICIOS))
mi, vecino = sys.argv[1].lower(), sys.argv[2].lower()
for s in (mi, vecino):
    if s not in SERVICIOS:
        salir(f"No existe el servicio '{s}'. Opciones: " + ", ".join(SERVICIOS))
if mi == vecino:
    salir("Tu servicio y el del vecino no pueden ser el mismo.")

for s in (mi, vecino):
    shutil.copy(f"contratos/{s}.proto", f"{s}.proto")

if os.path.exists("servidor.py"):
    print("servidor.py ya existe: no lo sobrescribo.")
else:
    shutil.copy(f"servicios/{mi}/servidor.py", "servidor.py")

v = SERVICIOS[vecino]
if os.path.exists("cliente_vecino.py"):
    print("cliente_vecino.py ya existe: no lo sobrescribo.")
else:
    open("cliente_vecino.py", "w", encoding="utf-8").write(f"""# Cliente del servicio {v['nombre']} (equipo vecino) · Reto de integración
# Contrato del vecino: {vecino}.proto · Qué hace y con qué datos probar: servicios/{vecino}/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import {vecino}_pb2
import {vecino}_pb2_grpc

canal = grpc.insecure_channel("localhost:{v['puerto']}")
stub = {vecino}_pb2_grpc.{v['clase']}Stub(canal)

print("=== Parte 1 · {v['unario']} con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.{v['unario']}(...) e imprime los campos de la respuesta.

print("=== Parte 2 · {v['unario']} con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.

print("=== Parte 3 · {v['stream']} (streaming) ===")
# TODO: recorre stub.{v['stream']}(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
""")

m = SERVICIOS[mi]
open("EQUIPO.md", "w", encoding="utf-8").write(f"""# Nuestro equipo

- **Nuestro servicio:** {m['nombre']} · puerto {m['puerto']} · contrato `{mi}.proto`
- **Servicio que consumimos (vecino):** {v['nombre']} · puerto {v['puerto']} · contrato `{vecino}.proto`
- **Repositorio del equipo vecino:** (pega aquí la URL)

| Integrante | Matrícula | Rol |
|---|---|---|
| | | Servidor |
| | | Cliente |
| | | Integración (README, issues y prueba cruzada) |

## Prueba cruzada

Corran `python cliente_vecino.py` contra el servidor **real** del equipo vecino (el que clonaron en `../vecino`)
y peguen aquí todo lo que imprimió:

```
(pega aquí la salida)
```

## Issues

Enlaces a los issues que abrieron en el repositorio del vecino o que les abrieron a ustedes (si hubo):

-

## Uso de IA (Acuerdo No. 23/2024 UdeC)

¿Usaron IA? ¿Cuál, quién y para qué? (por ejemplo: "Copilot para el for de la parte 3; lo revisamos línea por línea").

-
""")

print(f"""
Listo. Tu servicio: {m['nombre']} (puerto {m['puerto']}). Tu vecino: {v['nombre']} (puerto {v['puerto']}).
Se crearon: servidor.py, cliente_vecino.py, EQUIPO.md, {mi}.proto y {vecino}.proto

Siguiente paso:  bash compilar.sh
""")
