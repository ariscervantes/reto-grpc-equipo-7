# Servidor del servicio Catálogo · Reto de integración · Unidad II
# Contrato: catalogo.proto · Puerto: 50051
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import catalogo_pb2
import catalogo_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
PRODUCTOS = {
    "P001": ("Laptop 14 pulgadas", 1299900, "computo"),
    "P002": ("Mouse inalambrico", 29900, "accesorios"),
    "P003": ("Audifonos bluetooth", 89900, "audio"),
    "P004": ("Teclado mecanico", 119900, "accesorios"),
    "P005": ("Bocina portatil", 69900, "audio"),
    "P006": ("Monitor 24 pulgadas", 329900, "computo"),
}


class CatalogoServicio(catalogo_pb2_grpc.CatalogoServicer):

    def ObtenerProducto(self, request, context):
        # UNARIO: regresa UNA caja con return
        # TODO
        # Busca request.clave en PRODUCTOS.
        # Si no existe: context.abort(grpc.StatusCode.NOT_FOUND, "No existe el producto ...")
        # Si existe: regresa un catalogo_pb2.Producto con sus 4 campos.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar ObtenerProducto")

    def ListarCategoria(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        # TODO
        # Si request.categoria viene vacía: context.abort(grpc.StatusCode.INVALID_ARGUMENT, ...)
        # Si ningún producto tiene esa categoría: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si hay: por cada producto de esa categoría, espera 0.5 s y haz yield de un catalogo_pb2.Producto.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar ListarCategoria")


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
catalogo_pb2_grpc.add_CatalogoServicer_to_server(CatalogoServicio(), servidor)
servidor.add_insecure_port("[::]:50051")
servidor.start()
print("Servidor de Catálogo escuchando en el puerto 50051...")
servidor.wait_for_termination()
