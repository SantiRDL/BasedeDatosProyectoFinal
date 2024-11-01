from flask import Flask, jsonify, request
import mysql.connector
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    connection = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    return connection

@app.route('/instructores', methods=['POST'])
def add_instructor():
    data = request.json
    ci = data['ci']
    nombre = data['nombre']
    apellido = data['apellido']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO instructores (ci, nombre, apellido) VALUES (%s, %s, %s)", (ci, nombre, apellido))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Instructor added successfully"}), 201

@app.route('/instructores/<ci>', methods=['DELETE'])
def delete_instructor(ci):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM instructores WHERE ci = %s", (ci,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Instructor deleted successfully"}), 200

@app.route('/instructores/<ci>', methods=['PUT'])
def update_instructor(ci):
    data = request.json
    nombre = data['nombre']
    apellido = data['apellido']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE instructores SET nombre = %s, apellido = %s WHERE ci = %s", (nombre, apellido, ci))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Instructor updated successfully"}), 200

# Similar endpoints can be created for alumnos, turnos, actividades, etc.

if __name__ == '__main__':
    app.run(debug=True)