#!/usr/bin/env bash
# Genera el código Python de los contratos que están en esta carpeta.
# Vuelve a correrlo CADA VEZ que cambie un .proto.
set -e
shopt -s nullglob
protos=(*.proto)
if [ ${#protos[@]} -eq 0 ]; then
  echo "No hay contratos en esta carpeta. Primero corre: python preparar.py <tu_servicio> <servicio_vecino>"
  exit 1
fi
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. "${protos[@]}"
echo "Listo: se compilaron ${protos[*]}"
