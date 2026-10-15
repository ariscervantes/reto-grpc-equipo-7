# Servidor del servicio Carrito · Reto de integración · Unidad II
# Contrato: carrito.proto · Puerto: 50057
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import carrito_pb2
import carrito_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
PRECIOS = {"P001": 1299900, "P002": 29900, "P003": 89900, "P004": 119900, "P005": 69900, "P006": 329900}
CARRITOS = {
    "ana": [("P001", 1), ("P002", 1)],
    "luis": [("P003", 1), ("P005", 2)],
}


class CarritoServicio(carrito_pb2_grpc.CarritoServicer):

    def TotalCarrito(self, request, context):
        # UNARIO: regresa UNA caja con return
        # TODO
        # Si el usuario no tiene carrito: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si tiene: total = suma de PRECIOS[clave] * cantidad; artículos = suma de las cantidades.
        # Regresa un carrito_pb2.Total.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar TotalCarrito")

    def VerArticulos(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        # TODO
        # Si el usuario no tiene carrito: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si tiene: por cada artículo, espera 0.5 s y haz yield de un carrito_pb2.Articulo (subtotal = precio * cantidad).
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar VerArticulos")


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
carrito_pb2_grpc.add_CarritoServicer_to_server(CarritoServicio(), servidor)
servidor.add_insecure_port("[::]:50057")
servidor.start()
print("Servidor de Carrito escuchando en el puerto 50057...")
servidor.wait_for_termination()
