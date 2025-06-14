#el config es la conexion a la base de datos

#create engine es una funcion que crea el "motor" que nos conecta a la db
#EJ: engine = create_engine("postgresql://usuario:clave@localhost:5432/mydb")
from sqlalchemy import create_engine, text
#ORM(object relational mapper), con sql alchemi podemos volver objetos en lineas para sql
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from fastapi import Depends

# Cargar variables .env
load_dotenv()

#esta variable es la direcion, sea localhost o una direccion
DB_HOST = os.getenv("DB_HOST")
#aqui contenemos el puerto en una variable
DB_PORT = os.getenv("DB_PORT")
#el nombre de la bd
DB_NAME = os.getenv("DB_NAME")
#usuario con permisos
DB_USER = os.getenv("DB_USER")
#contraseña del usuario
DB_PASSWORD = os.getenv("DB_PASSWORD")

#este es un capturador de errores para las variables de acceso
missing = [var for var in [DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD] if var is None]
#este if muestra si el missing se activa y cierra secion
if missing:
    print("404 Variables de entorno faltantes.")
    exit()

#cadena de conexion a la base de datos postgresql, estamos usando el driver psycopg2
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#con este try catch se crea el engine que seria el motor de base de datos
try:
    #se crea un objeto de conexion general con la url pero no hay conexion
    engine = create_engine(DATABASE_URL)
    #aqui usamos el objeto y se conecta la api y bd
    with engine.connect() as connection:
        #aqui se ejecuta un comando sql, si funciona es que estamos conectados si no no
        connection.execute(text("SELECT 1"))
        print("Conexión exitosa a la base de datos.")
#este es el catch del try
except Exception as e:
    print("Error en la conexión:", e)
    engine = None

#session local es una funcion para dar una conexion a la bd con cada consulta
#entonces al agregar esta fabrica de sesiones puedo atender varias seciones sin problemas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) if engine else None

#la base es un bodelo para las tablas
Base = declarative_base()


# Función para inyectar sesiones de BD en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

