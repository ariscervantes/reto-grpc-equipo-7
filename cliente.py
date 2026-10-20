import grpc
import resenas_pb2
import resenas_pb2_grpc

def ejecutar():
    # 1. Conectarnos al servidor (mismo puerto 50053)
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = resenas_pb2_grpc.ResenasStub(channel)

        print("--- Consultando PromedioProducto para P003 ---")
        
        try:
            # 2. Hacemos la petición
            request = resenas_pb2.ResenaRequest(clave="P003")
            respuesta = stub.PromedioProducto(request)

            # 3. Imprimimos la respuesta
            print(f"Clave: {respuesta.clave}")
            print(f"Total de reseñas: {respuesta.total}")
            print(f"Promedio: {respuesta.promedio}")
            print(f"Reseñas de 5 estrellas: {respuesta.cinco_estrellas}")
            
            print("\n¡Éxito! El campo 'cinco_estrellas' se recibió correctamente.")

        except grpc.RpcError as e:
            print(f"Error en la llamada gRPC: {e.code()} - {e.details()}")

if __name__ == '__main__':
    ejecutar()