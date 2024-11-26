CREATE DATABASE IF NOT EXISTS escuela_deportes_nieve;

    USE escuela_deportes_nieve;

    -- Tabla de Login
    CREATE TABLE IF NOT EXISTS login (
        correo VARCHAR(100) PRIMARY KEY,
        contrasena VARCHAR(255) NOT NULL
    );

    -- Tabla de Actividades
    CREATE TABLE IF NOT EXISTS actividades (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descripcion VARCHAR(255) NOT NULL,
        costo DECIMAL(10, 2) NOT NULL
    );

    -- Tabla de Equipamiento
    CREATE TABLE IF NOT EXISTS equipamiento (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_actividad INT,
        descripcion VARCHAR(255) NOT NULL,
        costo DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (id_actividad) REFERENCES actividades(id)
    );

    -- Tabla de Instructores
    CREATE TABLE IF NOT EXISTS instructores (
        ci INT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL
    );

    -- Tabla de Turnos
    CREATE TABLE IF NOT EXISTS turnos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hora_inicio TIME NOT NULL,
        hora_fin TIME NOT NULL
    );

    -- Tabla de Alumnos
    CREATE TABLE IF NOT EXISTS alumnos (
        ci INT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        fecha_nacimiento DATE NOT NULL,
        telefono VARCHAR(20),
        correo VARCHAR(100) NOT NULL
    );

    -- Tabla de Clases
    CREATE TABLE IF NOT EXISTS clase (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ci_instructor INT,
        id_actividad INT,
        id_turno INT,
        dictada BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (ci_instructor) REFERENCES instructores(ci),
        FOREIGN KEY (id_actividad) REFERENCES actividades(id),
        FOREIGN KEY (id_turno) REFERENCES turnos(id)
    );

    -- Tabla de Alumno_Clase (relaciona alumnos con clases y equipos)
    CREATE TABLE IF NOT EXISTS alumno_clase (
        id_clase INT,
        ci_alumno INT,
        id_equipamiento INT,
        PRIMARY KEY (id_clase, ci_alumno),
        FOREIGN KEY (id_clase) REFERENCES clase(id),
        FOREIGN KEY (ci_alumno) REFERENCES alumnos(ci),
        FOREIGN KEY (id_equipamiento) REFERENCES equipamiento(id)
    );


    -- Insertar actividades
    INSERT INTO actividades (descripcion, costo) VALUES ('Snowboard', 50.00);
    INSERT INTO actividades (descripcion, costo) VALUES ('Ski', 45.00);

    -- Insertar equipamiento
    INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (1, 'Tabla de Snowboard', 10.00);
    INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (2, 'Esquí', 15.00);

    -- Insertar instructores
    INSERT INTO instructores (ci, nombre, apellido) VALUES (12345, 'Juan', 'Pérez');
    INSERT INTO instructores (ci, nombre, apellido) VALUES (67890, 'Ana', 'Gómez');

    -- Insertar turnos
    INSERT INTO turnos (hora_inicio, hora_fin) VALUES ('09:00', '11:00');
    INSERT INTO turnos (hora_inicio, hora_fin) VALUES ('12:00', '14:00');

    -- Insertar alumnos
    INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, telefono, correo) VALUES (10001, 'Carlos', 'Martínez', '1990-05-21', '091234567', 'carlos@ejemplo.com');
    INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, telefono, correo) VALUES (10002, 'Laura', 'Rodríguez', '1992-08-15', '092345678', 'laura@ejemplo.com');

    -- Insertar clases
    INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada) VALUES (12345, 1, 1, FALSE);
    INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada) VALUES (67890, 2, 2, FALSE);

    -- Insertar registros en alumno_clase
    INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento) VALUES (1, 10001, 1);
    INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento) VALUES (2, 10002, 2);