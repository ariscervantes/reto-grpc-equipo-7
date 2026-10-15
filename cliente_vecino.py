# Cliente del servicio Notificaciones (equipo vecino) · Reto de integración
# Contrato del vecino: notificaciones.proto · Qué hace y con qué datos probar: servicios/notificaciones/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import notificaciones_pb2
import notificaciones_pb2_grpc

canal = grpc.insecure_channel("localhost:50054")
stub = notificaciones_pb2_grpc.NotificacionesStub(canal)

print("=== Parte 1 · EnviarAviso con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.EnviarAviso(...) e imprime los campos de la respuesta.

print("=== Parte 2 · EnviarAviso con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.

print("=== Parte 3 · Suscribirse (streaming) ===")
# TODO: recorre stub.Suscribirse(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
