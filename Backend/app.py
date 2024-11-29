import sys
import MySQLdb
from config import Config

def get_db_connection():
    try:
        connection = MySQLdb.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            passwd=Config.MYSQL_PASSWORD,
            db=Config.MYSQL_DB
        )
        return connection
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

# Funciones para ABM de instructores
def add_instructor(ci, nombre, apellido):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO instructores (ci, nombre, apellido) VALUES (%s, %s, %s)", (ci, nombre, apellido))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error adding instructor: {e}")
    finally:
        cursor.close()
        connection.close()

def update_instructor(ci, nombre, apellido):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE instructores SET nombre = %s, apellido = %s WHERE ci = %s", (nombre, apellido, ci))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error updating instructor: {e}")
    finally:
        cursor.close()
        connection.close()

def delete_instructor(ci):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM instructores WHERE ci = %s", (ci,))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error deleting instructor: {e}")
    finally:
        cursor.close()
        connection.close()

# Funciones para ABM de turnos
def add_turno(descripcion):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO turnos (descripcion) VALUES (%s)", (descripcion,))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error adding turno: {e}")
    finally:
        cursor.close()
        connection.close()

def update_turno(id, descripcion):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE turnos SET descripcion = %s WHERE id = %s", (descripcion, id))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error updating turno: {e}")
    finally:
        cursor.close()
        connection.close()

def delete_turno(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM turnos WHERE id = %s", (id,))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error deleting turno: {e}")
    finally:
        cursor.close()
        connection.close()

# Funciones para modificación de actividades
def update_actividad(id, descripcion, costo, instructor, turno):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE actividades SET descripcion = %s, costo = %s, instructor = %s, turno = %s WHERE id = %s", (descripcion, costo, instructor, turno, id))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error updating actividad: {e}")
    finally:
        cursor.close()
        connection.close()

# Funciones para ABM de alumnos
def add_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s)", (ci, nombre, apellido, fecha_nacimiento, telefono, correo))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error adding alumno: {e}")
    finally:
        cursor.close()
        connection.close()

def update_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE alumnos SET nombre = %s, apellido = %s, fecha_nacimiento = %s, telefono = %s, correo = %s WHERE ci = %s", (nombre, apellido, fecha_nacimiento, telefono, correo, ci))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error updating alumno: {e}")
    finally:
        cursor.close()
        connection.close()

def delete_alumno(ci):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM alumnos WHERE ci = %s", (ci,))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error deleting alumno: {e}")
    finally:
        cursor.close()
        connection.close()

# Funciones para manejar las clases
def add_clase(ci_instructor, id_actividad, id_turno, dictada, turno, tipo_actividad):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Verificar que el instructor no tenga otra clase en el mismo turno
        cursor.execute("SELECT COUNT(*) FROM clase WHERE ci_instructor = %s AND turno = %s", (ci_instructor, turno))
        if cursor.fetchone()[0] > 0:
            print("El instructor ya tiene una clase en este turno.")
            return

        cursor.execute("INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada, turno, tipo_actividad) VALUES (%s, %s, %s, %s, %s, %s)", (ci_instructor, id_actividad, id_turno, dictada, turno, tipo_actividad))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error adding clase: {e}")
    finally:
        cursor.close()
        connection.close()

def update_clase(id, ci_instructor, id_turno):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Verificar que el instructor no tenga otra clase en el mismo turno
        cursor.execute("SELECT COUNT(*) FROM clase WHERE ci_instructor = %s AND id_turno = %s AND id != %s", (ci_instructor, id_turno, id))
        if cursor.fetchone()[0] > 0:
            print("El instructor ya tiene una clase en este turno.")
            return

        cursor.execute("UPDATE clase SET ci_instructor = %s, id_turno = %s WHERE id = %s", (ci_instructor, id_turno, id))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error updating clase: {e}")
    finally:
        cursor.close()
        connection.close()

def add_alumno_to_clase(id_clase, ci_alumno):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Verificar que el alumno no esté inscrito en otra clase en el mismo turno
        cursor.execute("SELECT turno FROM clase WHERE id = %s", (id_clase,))
        turno = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM clase c JOIN alumno_clase ac ON c.id = ac.id_clase WHERE ac.ci_alumno = %s AND c.turno = %s", (ci_alumno, turno))
        if cursor.fetchone()[0] > 0:
            print("El alumno ya está inscrito en otra clase en este turno.")
            return

        cursor.execute("INSERT INTO alumno_clase (id_clase, ci_alumno) VALUES (%s, %s)", (id_clase, ci_alumno))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error adding alumno to clase: {e}")
    finally:
        cursor.close()
        connection.close()

def remove_alumno_from_clase(id_clase, ci_alumno):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM alumno_clase WHERE id_clase = %s AND ci_alumno = %s", (id_clase, ci_alumno))
        connection.commit()
    except MySQLdb.Error as e:
        connection.rollback()
        print(f"Error removing alumno from clase: {e}")
    finally:
        cursor.close()
        connection.close()

# Funciones para los reportes
def get_actividades_ingresos():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT a.descripcion, SUM(e.costo) + SUM(c.costo) AS total_ingresos
            FROM clase c
            JOIN actividades a ON c.id_actividad = a.id
            LEFT JOIN equipamiento e ON c.id = e.id_actividad
            GROUP BY a.descripcion
            ORDER BY total_ingresos DESC
        """)
        report = cursor.fetchall()
        return report
    except MySQLdb.Error as e:
        print(f"Error fetching actividades ingresos: {e}")
    finally:
        cursor.close()
        connection.close()

def get_actividades_alumnos():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT a.descripcion, COUNT(ac.ci_alumno) AS total_alumnos
            FROM clase c
            JOIN actividades a ON c.id_actividad = a.id
            JOIN alumno_clase ac ON c.id = ac.id_clase
            GROUP BY a.descripcion
            ORDER BY total_alumnos DESC
        """)
        report = cursor.fetchall()
        return report
    except MySQLdb.Error as e:
        print(f"Error fetching actividades alumnos: {e}")
    finally:
        cursor.close()
        connection.close()

def get_turnos_clases():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT t.descripcion, COUNT(c.id) AS total_clases
            FROM clase c
            JOIN turnos t ON c.id_turno = t.id
            GROUP BY t.descripcion
            ORDER BY total_clases DESC
        """)
        report = cursor.fetchall()
        return report
    except MySQLdb.Error as e:
        print(f"Error fetching turnos clases: {e}")
    finally:
        cursor.close()
        connection.close()

# Funciones para imprimir los resultados
def print_report(report):
    for row in report:
        print(row)

def print_menu():
    print("\nMenu:")
    print("1. ABM de Instructores")
    print("2. ABM de Turnos")
    print("3. Modificación de Actividades")
    print("4. ABM de Alumnos")
    print("5. Manejo de Clases")
    print("6. Reportes")
    print("7. Salir")

def print_submenu(title, options):
    print(f"\n{title}:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print(f"{len(options) + 1}. Volver al menú principal")

def main():
    while True:
        print_menu()
        choice = input("Seleccione una opción: ")
        if choice == '1':
            abm_instructores()
        elif choice == '2':
            abm_turnos()
        elif choice == '3':
            modificacion_actividades()
        elif choice == '4':
            abm_alumnos()
        elif choice == '5':
            manejo_clases()
        elif choice == '6':
            reportes()
        elif choice == '7':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def abm_instructores():
    options = ["Agregar Instructor", "Modificar Instructor", "Eliminar Instructor"]
    while True:
        print_submenu("ABM de Instructores", options)
        choice = input("Seleccione una opción: ")
        if choice == '1':
            ci = input("CI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            add_instructor(ci, nombre, apellido)
        elif choice == '2':
            ci = input("CI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            update_instructor(ci, nombre, apellido)
        elif choice == '3':
            ci = input("CI: ")
            delete_instructor(ci)
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def abm_turnos():
    options = ["Agregar Turno", "Modificar Turno", "Eliminar Turno"]
    while True:
        print_submenu("ABM de Turnos", options)
        choice = input("Seleccione una opción: ")
        if choice == '1':
            descripcion = input("Descripción: ")
            add_turno(descripcion)
        elif choice == '2':
            id = input("ID: ")
            descripcion = input("Descripción: ")
            update_turno(id, descripcion)
        elif choice == '3':
            id = input("ID: ")
            delete_turno(id)
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def modificacion_actividades():
    options = ["Modificar Actividad"]
    while True:
        print_submenu("Modificación de Actividades", options)
        choice = input("Seleccione una opción: ")
        if choice == '1':
            id = input("ID: ")
            descripcion = input("Descripción: ")
            costo = input("Costo: ")
            instructor = input("Instructor: ")
            turno = input("Turno: ")
            update_actividad(id, descripcion, costo, instructor, turno)
        elif choice == '2':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def abm_alumnos():
    options = ["Agregar Alumno", "Modificar Alumno", "Eliminar Alumno"]
    while True:
        print_submenu("ABM de Alumnos", options)
        choice = input("Seleccione una opción: ")
        if choice == '1':
            ci = input("CI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            add_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo)
        elif choice == '2':
            ci = input("CI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            update_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo)
        elif choice == '3':
            ci = input("CI: ")
            delete_alumno(ci)
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def manejo_clases():
    options = ["Agregar Clase", "Modificar Clase", "Agregar Alumno a Clase", "Quitar Alumno de Clase"]
    while True:
        print_submenu("Manejo de Clases", options)
        choice = input("Seleccione una opción: ")
        if choice == '1':
            ci_instructor = input("CI del Instructor: ")
            id_actividad = input("ID de la Actividad: ")
            id_turno = input("ID del Turno: ")
            dictada = input("Dictada (1 para Sí, 0 para No): ")
            turno = input("Turno: ")
            tipo_actividad = input("Tipo de Actividad (grupal/individual): ")
            add_clase(ci_instructor, id_actividad, id_turno, dictada, turno, tipo_actividad)
        elif choice == '2':
            id = input("ID de la Clase: ")
            ci_instructor = input("CI del Instructor: ")
            id_turno = input("ID del Turno: ")
            update_clase(id, ci_instructor, id_turno)
        elif choice == '3':
            id_clase = input("ID de la Clase: ")
            ci_alumno = input("CI del Alumno: ")
            add_alumno_to_clase(id_clase, ci_alumno)
        elif choice == '4':
            id_clase = input("ID de la Clase: ")
            ci_alumno = input("CI del Alumno: ")
            remove_alumno_from_clase(id_clase, ci_alumno)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def reportes():
    options = ["Actividades que más ingresos generan", "Actividades con más alumnos", "Turnos con más clases dictadas"]
    while True:
        print_submenu("Reportes", options)
        choice = input("Seleccione una opción: ")
        if choice == '1':
            report = get_actividades_ingresos()
            print_report(report)
        elif choice == '2':
            report = get_actividades_alumnos()
            print_report(report)
        elif choice == '3':
            report = get_turnos_clases()
            print_report(report)
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()