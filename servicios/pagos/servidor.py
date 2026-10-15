# Servidor del servicio Pagos · Reto de integración · Unidad II
# Contrato: pagos.proto · Puerto: 50056
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import pagos_pb2
import pagos_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
PEDIDOS = {
    "PED-100": (True, 1329800),
    "PED-101": (False, 89900),
}
PASOS = ["Validando datos", "Autorizando con el banco", "Cobro aprobado"]


class PagosServicio(pagos_pb2_grpc.PagosServicer):

    def ConsultarPago(self, request, context):
        # UNARIO: regresa UNA caja con return
        # TODO
        # Si el pedido no existe: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si existe: regresa un pagos_pb2.EstadoPago con pedido, pagado y monto.
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar ConsultarPago")

    def SeguirCobro(self, request, context):
        # STREAMING: entrega VARIAS cajas con yield
        # TODO
        # Si monto_centavos es 0 o menor: context.abort(grpc.StatusCode.INVALID_ARGUMENT, ...)
        # Si no: por cada paso de PASOS, espera 1 s y haz yield de un pagos_pb2.PasoCobro (numero 1, 2, 3).
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Falta implementar SeguirCobro")


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
pagos_pb2_grpc.add_PagosServicer_to_server(PagosServicio(), servidor)
servidor.add_insecure_port("[::]:50056")
servidor.start()
print("Servidor de Pagos escuchando en el puerto 50056...")
servidor.wait_for_termination()
