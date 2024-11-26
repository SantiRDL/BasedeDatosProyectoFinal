import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',  # Nombre del contenedor de MySQL en Docker
        user='root',             # Nombre de usuario (definido en docker-compose.yml)
        password='rootpassword', # Contraseña (definida en docker-compose.yml)
        database='escuela_deportes_nieve',  # Nombre de la base de datos
        port=3306                # Puerto por defecto de MySQL
    )