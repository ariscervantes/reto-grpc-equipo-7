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