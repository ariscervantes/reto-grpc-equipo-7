# Servidor del servicio Notificaciones · Reto de integración · Unidad II
# Contrato: notificaciones.proto · Puerto: 50054
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import notificaciones_pb2
import notificaciones_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
AVISOS = {
    "ana": ["Tu pedido PED-100 fue pagado", "Tu paquete GUIA-500 va en camino", "Tienes una nueva resena"],
    "luis": ["Tu carrito tiene 2 articulos"],
}
CONTADOR = [1000]


class NotificacionesServicio(notificaciones_pb2_grpc.NotificacionesServicer):

    def EnviarAviso(self, request, context):
        # UNARIO: regresa UNA caja con return
        # TODO
        # Si request.destinatario o request.mensaje vienen vacíos: context.abort(grpc.StatusCode.INVALID_ARGUMENT, ...)
        # Si no: agrega el mensaje a AVISOS[destinatario] (créalo si no existe).
        # Regresa una Confirmacion con un folio "AV-1001", "AV-1002"… (usa CONTADOR) y entregado=True.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar EnviarAviso")

    def Suscribirse(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        # TODO
        # Si el destinatario no tiene avisos: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si tiene: por cada aviso, espera 1 s y haz yield de un notificaciones_pb2.Aviso.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar Suscribirse")


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
notificaciones_pb2_grpc.add_NotificacionesServicer_to_server(NotificacionesServicio(), servidor)
servidor.add_insecure_port("[::]:50054")
servidor.start()
print("Servidor de Notificaciones escuchando en el puerto 50054...")
servidor.wait_for_termination()
