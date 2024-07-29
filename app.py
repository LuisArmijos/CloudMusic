from flask import Flask, render_template
import psycopg2
import os
from dotenv import load_dotenv
import boto3

app = Flask(__name__)

load_dotenv() # Para cargar las variables de entorno

# Configuración de la base de datos
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        dbname=os.getenv('DB_NAME')
    )
    return conn

# Configuración de AWS S3 usando variables de entorno
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION') 
)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT nombre, artista, album, ruta FROM canciones;')
    canciones = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('index.html', canciones=canciones)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
