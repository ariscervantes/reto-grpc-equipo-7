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
        resenas = RESENAS.get(request.clave)
        if not resenas:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"El producto {request.clave} no tiene reseñas",
            )

        total = len(resenas)
        suma = sum(estrellas for _, estrellas, _ in resenas)
        return resenas_pb2.Promedio(
            clave=request.clave,
            promedio=suma / total,
            total=total,
        )

    def ListarResenas(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        resenas = RESENAS.get(request.clave)
        if not resenas:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"El producto {request.clave} no tiene reseñas",
            )

        for autor, estrellas, comentario in resenas:
            time.sleep(0.5)
            yield resenas_pb2.Resena(
                autor=autor,
                estrellas=estrellas,
                comentario=comentario,
            )
            

servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
resenas_pb2_grpc.add_ResenasServicer_to_server(ResenasServicio(), servidor)
servidor.add_insecure_port("[::]:50053")
servidor.start()
print("Servidor de Reseñas escuchando en el puerto 50053...")
servidor.wait_for_termination()