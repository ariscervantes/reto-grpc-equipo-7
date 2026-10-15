# Equipo 7 — Servicio de Reseñas

**Materia:** Programación Distribuida  
**Institución:** Universidad de Colima  
**Facultad:** Facultad de Telemática  
**Proyecto:** Reto de integración — Tienda en línea con gRPC

## 1. Integrantes y responsabilidades

| Integrante | Matrícula | Rol y actividades realizadas |
|---|---|---|
| Arisbeth Cervantes | 20204413 | Desarrollo del cliente gRPC para consumir el servicio de Notificaciones del equipo 5. Implementación de las operaciones `EnviarAviso` y `Suscribirse`, manejo de errores y pruebas de comunicación. |
| Teresa Torres | 20206615 | Documentación y pruebas: elaboración y organización de la documentación del proyecto en EQUIPO.md, ejecución y registro de pruebas funcionales y de integración, así como recopilación de evidencias de los resultados obtenidos. |
| Cesar Vergara | 20204927 | Implementación del servidor gRPC de Reseñas, incluyendo las operaciones `PromedioProducto` y `ListarResenas`, el cálculo de promedios y el manejo de errores `NOT_FOUND`. |

## 2. Repositorios utilizados

### Repositorio del equipo 7

https://github.com/ariscervantes/reto-grpc-equipo-7

**Servicio desarrollado:** Reseñas  
**Puerto:** 50053  
**Contrato:** `resenas.proto`

### Repositorio del equipo vecino

**Equipo:** 5  
**Servicio:** Notificaciones  
**Puerto:** 50054

**URL del repositorio:** https://github.com/Bb3t0-V4zf1g/reto-tienda

El equipo 7 consume el servicio de Notificaciones desarrollado por el equipo 5 mediante un cliente gRPC implementado en `cliente_vecino.py`.

La comunicación utiliza el contrato definido en `notificaciones.proto`.

## 3. Implementación del servicio de Reseñas

El equipo 7 desarrolló un servidor gRPC para consultar las reseñas de los productos de una tienda en línea.

Se implementaron dos operaciones:

### PromedioProducto

Operación unaria que recibe la clave de un producto y devuelve:

- Clave del producto.
- Promedio de calificaciones.
- Cantidad total de reseñas.

Cuando el producto no tiene reseñas, el servidor devuelve el código gRPC `NOT_FOUND`.

### ListarResenas

Operación de tipo server streaming que recibe la clave de un producto y devuelve sus reseñas individualmente.

Cada reseña contiene:

- Autor.
- Cantidad de estrellas.
- Comentario.

El servidor utiliza `yield` para enviar las respuestas de manera secuencial.

Cuando el producto no tiene reseñas, devuelve `NOT_FOUND`.

### Pruebas realizadas al servidor

Se realizaron pruebas locales mediante un cliente gRPC temporal para verificar ambas operaciones.

**Prueba 1. PromedioProducto con P001**

```text
Producto: P001
Promedio: 4.5
Total de reseñas: 2
```

**Prueba 2. PromedioProducto con P003**

```text
Producto: P003
Promedio: 3.67
Total: 3
```

**Prueba 3. ListarResenas con P003**

```text
Consultando reseñas del producto P003...

Reseña 1
Autor: said
Estrellas: 5
Comentario: Gran sonido
------------------------------
Reseña 2
Autor: omar
Estrellas: 4
Comentario: Comodos
------------------------------
Reseña 3
Autor: ana
Estrellas: 2
Comentario: Se desconectan
------------------------------
```

**Prueba 4. Manejo de errores NOT_FOUND**

```text
Producto: P004
PromedioProducto: NOT_FOUND
ListarResenas: NOT_FOUND

Producto: P006
PromedioProducto: NOT_FOUND
ListarResenas: NOT_FOUND

Producto: P999
PromedioProducto: NOT_FOUND
ListarResenas: NOT_FOUND
```

Los resultados anteriores corresponden a pruebas locales del servidor del equipo 7.

## 4. Cliente del servicio de Notificaciones

Se implementó un cliente gRPC para consumir el servicio de Notificaciones del equipo 5.

El cliente se encuentra en el archivo `cliente_vecino.py`.

### Operaciones implementadas

**EnviarAviso (unaria)**

Se construye una solicitud de tipo `Aviso`, proporcionando un destinatario y un mensaje.

El cliente obtiene una respuesta `Confirmacion` con los campos:

- `folio`
- `entregado`

También se implementó una prueba con un mensaje vacío para comprobar el código de error `INVALID_ARGUMENT`.

**Suscribirse (server streaming)**

Se construye una solicitud `Suscripcion` con el destinatario correspondiente.

El cliente utiliza un ciclo `for` para recorrer los avisos recibidos y mostrar sus datos.

Las operaciones incluyen manejo de excepciones mediante `grpc.RpcError`.

## 5. Prueba cruzada con el equipo 5

**Repositorio del equipo 5:** https://github.com/Bb3t0-V4zf1g/reto-tienda

**Servicio consumido:** Notificaciones

**Fecha de la prueba:** 15/10/2025

**Entorno de ejecución:** GitHub Codespaces / Python / gRPC

### Procedimiento

1. Se obtuvo el repositorio del equipo 5.
2. Se inició el servidor real de Notificaciones en el puerto 50054.
3. Se ejecutó el cliente `cliente_vecino.py` del equipo 7.
4. Se verificó el envío de un aviso válido.
5. Se comprobó el manejo del error `INVALID_ARGUMENT`.
6. Se probó la recepción de avisos mediante server streaming.

### Salida real de la prueba cruzada

Ejecutar:

```bash
python cliente_vecino.py
```


```text
s/reto-grpc-equipo-7 (main) $ python cliente_vecino.py

=== Parte 1 · EnviarAviso con un dato válido ===
Folio: AV-1001
Entregado: True

=== Parte 2 · EnviarAviso con un dato que provoca error ===
Código: INVALID_ARGUMENT
Detalle: destinatario y mensaje son obligatorios

=== Parte 3 · Suscribirse (streaming) ===

Aviso 1
Destinatario: ana
Mensaje: Tu pedido PED-100 fue pagado

Aviso 2
Destinatario: ana
Mensaje: Tu paquete GUIA-500 va en camino

Aviso 3
Destinatario: ana
Mensaje: Tienes una nueva resena

Aviso 4
Destinatario: ana
Mensaje: Hola
((.venv) ) @ariscervantes ➜ /workspace
s/reto-grpc-equipo-7 (main) $ 
```

## 6. Issues y seguimiento de incidencias

**Repositorio:** https://github.com/ariscervantes/reto-grpc-equipo-7

Durante las pruebas locales se identificaron dificultades relacionadas con la instalación de dependencias de Protocol Buffers y la configuración de rutas de importación de Python.

Estas dificultades se resolvieron mediante la revisión del entorno virtual y la configuración de `PYTHONPATH`.

## 7. Declaración de uso de inteligencia artificial

En atención al Acuerdo No. 23/2024 de la Universidad de Colima, se declara el uso de herramientas de inteligencia artificial generativa como apoyo durante el desarrollo del proyecto.

### Herramientas utilizadas

**Herramienta:** ChatGPT (OpenAI)

**Finalidad del uso:**

- Orientación para configurar el entorno de desarrollo en GitHub Codespaces.
- Apoyo en la identificación y solución de errores relacionados con dependencias de Python y Protocol Buffers.
- Asistencia para comprender la comunicación entre clientes y servidores gRPC.
- Apoyo en la implementación del cliente de Notificaciones.
- Orientación para implementar el manejo de excepciones mediante `grpc.RpcError`.
- Explicación de las diferencias entre operaciones unarias y server streaming.
- Apoyo en la elaboración y organización de la documentación del proyecto.

**Participación humana:**

La configuración del entorno, la ejecución de los programas, la realización de pruebas y la revisión de los resultados se llevaron a cabo por los integrantes del equipo.

El uso de inteligencia artificial se realizó como herramienta de apoyo técnico y educativo. Las respuestas y sugerencias fueron revisadas mediante la ejecución y comprobación del funcionamiento del software.