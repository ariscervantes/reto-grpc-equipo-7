# Servidor del servicio Reseñas · Reto de integración · Unidad II
# Contrato: resenas.proto · Puerto: 50053
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import resenas_pb2
import resenas_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
RESENAS = {
    "P001": [("ana", 5, "Rapida y ligera"), ("luis", 4, "Buena bateria")],
    "P002": [("mayte", 3, "Cumple")],
    "P003": [("said", 5, "Gran sonido"), ("omar", 4, "Comodos"), ("ana", 2, "Se desconectan")],
    "P005": [("diego", 4, "Suena fuerte")],
}


class ResenasServicio(resenas_pb2_grpc.ResenasServicer):

    def PromedioProducto(self, request, context):
        # UNARIO: regresa UNA caja con return
        # TODO
        # Si el producto no tiene reseñas: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si tiene: calcula el promedio de estrellas y el total de reseñas.
        # Regresa un resenas_pb2.Promedio.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar PromedioProducto")

    def ListarResenas(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        # TODO
        # Si el producto no tiene reseñas: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si tiene: por cada reseña, espera 0.5 s y haz yield de un resenas_pb2.Resena.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar ListarResenas")


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
resenas_pb2_grpc.add_ResenasServicer_to_server(ResenasServicio(), servidor)
servidor.add_insecure_port("[::]:50053")
servidor.start()
print("Servidor de Reseñas escuchando en el puerto 50053...")
servidor.wait_for_termination()
