# Servidor del servicio Inventario · Reto de integración · Unidad II
# Contrato: inventario.proto · Puerto: 50052
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import inventario_pb2
import inventario_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
EXISTENCIAS = {
    "P001": (5, "Colima"),
    "P002": (40, "Colima"),
    "P003": (12, "Manzanillo"),
    "P004": (0, "Colima"),
    "P005": (7, "Tecoman"),
    "P006": (3, "Colima"),
}


class InventarioServicio(inventario_pb2_grpc.InventarioServicer):

    def ConsultarExistencia(self, request, context):
        # UNARIO: regresa UNA caja con return
        # TODO
        # Busca request.clave en EXISTENCIAS.
        # Si no existe: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si existe: regresa un inventario_pb2.Existencia con clave, cantidad y almacén.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar ConsultarExistencia")

    def VigilarExistencia(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        # TODO
        # Si la clave no existe: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si existe: manda 4 actualizaciones, una por segundo.
        # En cada una la cantidad baja en 1 (simula una venta), sin bajar de 0.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar VigilarExistencia")


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
inventario_pb2_grpc.add_InventarioServicer_to_server(InventarioServicio(), servidor)
servidor.add_insecure_port("[::]:50052")
servidor.start()
print("Servidor de Inventario escuchando en el puerto 50052...")
servidor.wait_for_termination()
