# WebApp Proyecto Final: Cloud Music

## Descripción

Este proyecto final consiste en desarrollar y desplegar una WebApp para la gestión de música utilizando servicios de Amazon Web Services (AWS). 
La WebApp está alojada en un servidor EC2 y utilizá un bucket de S3 para almacenar archivos mp3. 
También se utilizará una base de datos RDS para almacenar información sobre las canciones. 
La aplicación debe permitir listar y reproducir canciones almacenadas en S3 desde una interfaz web.

## Requisitos

 **Flask**: Framework web en Python para desarrollar la WebApp.
- **boto3**: SDK de AWS para Python que permite la interacción con servicios de AWS como S3 y RDS.
- **psycopg2-binary**: Adaptador PostgreSQL para Python, utilizado para conectar la WebApp con la base de datos RDS.
- **python-dotenv**: Biblioteca para cargar variables de entorno desde un archivo `.env`.

## Autor

Luis Armijos

