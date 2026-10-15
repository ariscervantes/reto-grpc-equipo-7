import grpc

import notificaciones_pb2
import notificaciones_pb2_grpc


def main():
    # Crear conexión con el servidor de Notificaciones
    canal = grpc.insecure_channel("localhost:50054")
    stub = notificaciones_pb2_grpc.NotificacionesStub(canal)

    # PARTE 1: Enviar un aviso válido
    print("\n=== Parte 1 · EnviarAviso con un dato válido ===")

    try:
        aviso = notificaciones_pb2.Aviso(
            destinatario="ana",
            mensaje="Hola"
        )

        respuesta = stub.EnviarAviso(aviso, timeout=5)

        print("Folio:", respuesta.folio)
        print("Entregado:", respuesta.entregado)

    except grpc.RpcError as error:
        print("Error:", error.code().name)
        print("Detalle:", error.details())

    # PARTE 2: Enviar un aviso inválido
    print("\n=== Parte 2 · EnviarAviso con un dato que provoca error ===")

    try:
        aviso_invalido = notificaciones_pb2.Aviso(
            destinatario="ana",
            mensaje=""
        )

        stub.EnviarAviso(aviso_invalido, timeout=5)

        print("ERROR: Se esperaba INVALID_ARGUMENT")

    except grpc.RpcError as error:
        print("Código:", error.code().name)
        print("Detalle:", error.details())

    # PARTE 3: Suscribirse y recibir avisos mediante streaming
    print("\n=== Parte 3 · Suscribirse (streaming) ===")

    try:
        suscripcion = notificaciones_pb2.Suscripcion(
            destinatario="ana"
        )

        respuestas = stub.Suscribirse(suscripcion, timeout=15)

        for numero, aviso in enumerate(respuestas, start=1):
            print(f"\nAviso {numero}")
            print("Destinatario:", aviso.destinatario)
            print("Mensaje:", aviso.mensaje)

    except grpc.RpcError as error:
        print("Código:", error.code().name)
        print("Detalle:", error.details())

    finally:
        canal.close()


if __name__ == "__main__":
    main()