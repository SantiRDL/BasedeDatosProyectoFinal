from flask import Blueprint, request, jsonify
from app.db_config import get_db_connection

# Crea un Blueprint
routes = Blueprint("routes", __name__)


# Ruta para obtener instructores
@routes.route('/api/instructors', methods=['GET'])
def get_instructors():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM instructores")
        result = cursor.fetchall()

        cursor.close()
        connection.close()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para crear un instructor
@routes.route('/api/instructors', methods=['POST'])
def create_instructor():
    data = request.json  # Recibe los datos enviados en formato JSON
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Insertar datos en la tabla instructores
        query = "INSERT INTO instructores (ci, nombre, apellido) VALUES (%s, %s, %s)"
        values = (data['ci'], data['nombre'], data['apellido'])
        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()
        return jsonify({"message": "Instructor creado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rutas para Actividades

@routes.route('/api/activities', methods=['GET'])
def get_activities():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM actividades")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

@routes.route('/api/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM actividades WHERE id = %s", (activity_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Actividad no encontrada"}), 404

@routes.route('/api/activities', methods=['POST'])
def create_activity():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO actividades (descripcion, costo) VALUES (%s, %s)", 
                   (data['description'], data['cost']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Actividad creada correctamente"}), 201

@routes.route('/api/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE actividades SET descripcion = %s, costo = %s WHERE id = %s", 
                   (data['description'], data['cost'], activity_id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Actividad actualizada correctamente"})

@routes.route('/api/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM actividades WHERE id = %s", (activity_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Actividad eliminada correctamente"})

# Rutas para Alumnos

@routes.route('/api/students', methods=['GET'])
def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alumnos")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

@routes.route('/api/students/<string:ci>', methods=['GET'])
def get_student(ci):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alumnos WHERE ci = %s", (ci,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Alumno no encontrado"}), 404

@routes.route('/api/students', methods=['POST'])
def create_student():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento) VALUES (%s, %s, %s, %s)", 
                   (data['ci'], data['name'], data['surname'], data['birthdate']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Alumno creado correctamente"}), 201

@routes.route('/api/students/<string:ci>', methods=['PUT'])
def update_student(ci):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE alumnos SET nombre = %s, apellido = %s, fecha_nacimiento = %s WHERE ci = %s", 
                   (data['name'], data['surname'], data['birthdate'], ci))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Alumno actualizado correctamente"})

@routes.route('/api/students/<string:ci>', methods=['DELETE'])
def delete_student(ci):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM alumnos WHERE ci = %s", (ci,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Alumno eliminado correctamente"})


# Rutas para Turnos

@routes.route('/api/turns', methods=['GET'])
def get_turns():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM turnos")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

@routes.route('/api/turns', methods=['POST'])
def create_turn():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO turnos (hora_inicio, hora_fin) VALUES (%s, %s)", 
                   (data['start_time'], data['end_time']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Turno creado correctamente"}), 201



# Rutas para Clases

@routes.route('/api/classes', methods=['GET'])
def get_classes():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clase")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

@routes.route('/api/classes', methods=['POST'])
def create_class():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada) VALUES (%s, %s, %s, %s)", 
                   (data['instructor_ci'], data['activity_id'], data['turn_id'], data['dictated']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Clase creada correctamente"}), 201
