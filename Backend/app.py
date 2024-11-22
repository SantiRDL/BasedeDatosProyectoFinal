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

# CRUD para la tabla login
@app.route('/login', methods=['POST'])
def add_login():
    data = request.json
    correo = data['correo']
    contraseña = data['contraseña']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO login (correo, contraseña) VALUES (%s, %s)", (correo, contraseña))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Login added successfully"}), 201

@app.route('/login/<correo>', methods=['GET'])
def get_login(correo):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM login WHERE correo = %s", (correo,))
    login = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if login:
        return jsonify({"correo": login[0], "contraseña": login[1]})
    else:
        return jsonify({"message": "Login not found"}), 404

@app.route('/login/<correo>', methods=['PUT'])
def update_login(correo):
    data = request.json
    contraseña = data['contraseña']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE login SET contraseña = %s WHERE correo = %s", (contraseña, correo))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Login updated successfully"})

@app.route('/login/<correo>', methods=['DELETE'])
def delete_login(correo):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM login WHERE correo = %s", (correo,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Login deleted successfully"})

# CRUD para la tabla actividades
@app.route('/actividades', methods=['POST'])
def add_actividad():
    data = request.json
    descripcion = data['descripcion']
    costo = data['costo']
    instructor = data.get('instructor')
    turno = data.get('turno')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO actividades (descripcion, costo, instructor, turno) VALUES (%s, %s, %s, %s)", (descripcion, costo, instructor, turno))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Actividad added successfully"}), 201

@app.route('/actividades/<id>', methods=['GET'])
def get_actividad(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM actividades WHERE id = %s", (id,))
    actividad = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if actividad:
        return jsonify({"id": actividad[0], "descripcion": actividad[1], "costo": actividad[2], "instructor": actividad[3], "turno": actividad[4]})
    else:
        return jsonify({"message": "Actividad not found"}), 404

@app.route('/actividades/<id>', methods=['PUT'])
def update_actividad(id):
    data = request.json
    descripcion = data['descripcion']
    costo = data['costo']
    instructor = data.get('instructor')
    turno = data.get('turno')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE actividades SET descripcion = %s, costo = %s, instructor = %s, turno = %s WHERE id = %s", (descripcion, costo, instructor, turno, id))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Actividad updated successfully"})

@app.route('/actividades/<id>', methods=['DELETE'])
def delete_actividad(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM actividades WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Actividad deleted successfully"})

# CRUD para la tabla equipamiento
@app.route('/equipamiento', methods=['POST'])
def add_equipamiento():
    data = request.json
    id_actividad = data['id_actividad']
    descripcion = data['descripcion']
    costo = data['costo']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (%s, %s, %s)", (id_actividad, descripcion, costo))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Equipamiento added successfully"}), 201

@app.route('/equipamiento/<id>', methods=['GET'])
def get_equipamiento(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM equipamiento WHERE id = %s", (id,))
    equipamiento = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if equipamiento:
        return jsonify({"id": equipamiento[0], "id_actividad": equipamiento[1], "descripcion": equipamiento[2], "costo": equipamiento[3]})
    else:
        return jsonify({"message": "Equipamiento not found"}), 404

@app.route('/equipamiento/<id>', methods=['PUT'])
def update_equipamiento(id):
    data = request.json
    id_actividad = data['id_actividad']
    descripcion = data['descripcion']
    costo = data['costo']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE equipamiento SET id_actividad = %s, descripcion = %s, costo = %s WHERE id = %s", (id_actividad, descripcion, costo, id))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Equipamiento updated successfully"})

@app.route('/equipamiento/<id>', methods=['DELETE'])
def delete_equipamiento(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM equipamiento WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Equipamiento deleted successfully"})

# CRUD para la tabla alumnos
@app.route('/alumnos', methods=['POST'])
def add_alumno():
    data = request.json
    nombre = data['nombre']
    ci = data['ci']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO alumnos (nombre, ci) VALUES (%s, %s)", (nombre, ci))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Alumno added successfully"}), 201

@app.route('/alumnos/<id>', methods=['GET'])
def get_alumno(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE id = %s", (id,))
    alumno = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if alumno:
        return jsonify({"id": alumno[0], "nombre": alumno[1], "ci": alumno[2]})
    else:
        return jsonify({"message": "Alumno not found"}), 404

@app.route('/alumnos/<id>', methods=['PUT'])
def update_alumno(id):
    data = request.json
    nombre = data['nombre']
    ci = data['ci']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE alumnos SET nombre = %s, ci = %s WHERE id = %s", (nombre, ci, id))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Alumno updated successfully"})

@app.route('/alumnos/<id>', methods=['DELETE'])
def delete_alumno(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Alumno deleted successfully"})

# CRUD para la tabla clases_grupales
@app.route('/clases_grupales', methods=['POST'])
def add_clase_grupal():
    data = request.json
    id_actividad = data['id_actividad']
    id_alumno = data['id_alumno']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO clases_grupales (id_actividad, id_alumno) VALUES (%s, %s)", (id_actividad, id_alumno))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Clase grupal added successfully"}), 201

@app.route('/clases_grupales/<id_actividad>/<id_alumno>', methods=['GET'])
def get_clase_grupal(id_actividad, id_alumno):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clases_grupales WHERE id_actividad = %s AND id_alumno = %s", (id_actividad, id_alumno))
    clase_grupal = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if clase_grupal:
        return jsonify({"id_actividad": clase_grupal[0], "id_alumno": clase_grupal[1]})
    else:
        return jsonify({"message": "Clase grupal not found"}), 404

@app.route('/clases_grupales/<id_actividad>/<id_alumno>', methods=['DELETE'])
def delete_clase_grupal(id_actividad, id_alumno):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM clases_grupales WHERE id_actividad = %s AND id_alumno = %s", (id_actividad, id_alumno))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Clase grupal deleted successfully"})

@app.route('/inscripciones', methods=['POST'])
def add_inscripcion():
    data = request.json
    id_clase = data['id_clase']
    ci_alumno = data['ci_alumno']
    id_equipamiento = data['id_equipamiento']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento) VALUES (%s, %s, %s)", (id_clase, ci_alumno, id_equipamiento))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Inscripción added successfully"}), 201

@app.route('/inscripciones', methods=['GET'])
def get_inscripciones():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT ac.id_clase, a.nombre AS nombre_alumno, a.apellido AS apellido_alumno, c.descripcion AS descripcion_clase, e.descripcion AS descripcion_equipamiento
        FROM alumno_clase ac
        JOIN alumnos a ON ac.ci_alumno = a.ci
        JOIN clase c ON ac.id_clase = c.id
        JOIN equipamiento e ON ac.id_equipamiento = e.id
    """)
    inscripciones = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return jsonify(inscripciones)

if __name__ == '__main__':
    app.run(debug=True)