# Servidor del servicio Envíos · Reto de integración · Unidad II
# Contrato: envios.proto · Puerto: 50055
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import envios_pb2
import envios_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
GUIAS = {
    "GUIA-500": [("Recibido", "Colima"), ("En bodega", "Colima"), ("En camino", "Manzanillo"), ("Entregado", "Manzanillo")],
    "GUIA-501": [("Recibido", "Colima"), ("En camino", "Guadalajara")],
}


class EnviosServicio(envios_pb2_grpc.EnviosServicer):

    def CotizarEnvio(self, request, context):
        # UNARIO: regresa UNA caja con return
        # TODO
        # Si el código postal no tiene exactamente 5 dígitos, o el peso es 0 o menor: context.abort(grpc.StatusCode.INVALID_ARGUMENT, ...)
        # Costo = 9900 + 2000 por cada kilo completo (peso_gramos // 1000 * 2000).
        # Días = 1 si el código postal empieza con "28" (Colima); si no, 3.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar CotizarEnvio")

    def Rastrear(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        # TODO
        # Si la guía no existe: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si existe: por cada estado, espera 1 s y haz yield de un envios_pb2.EstadoEnvio.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar Rastrear")


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
envios_pb2_grpc.add_EnviosServicer_to_server(EnviosServicio(), servidor)
servidor.add_insecure_port("[::]:50055")
servidor.start()
print("Servidor de Envíos escuchando en el puerto 50055...")
servidor.wait_for_termination()
