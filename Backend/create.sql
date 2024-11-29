CREATE DATABASE escuela_deportes_nieve;

USE escuela_deportes_nieve;

CREATE TABLE login (
    correo VARCHAR(255) PRIMARY KEY,
    contraseña VARCHAR(255) NOT NULL
);

CREATE TABLE actividades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    instructor VARCHAR(255),
    turno VARCHAR(255)
);

CREATE TABLE equipamiento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_actividad INT,
    descripcion VARCHAR(255) NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_actividad) REFERENCES actividades(id)
);

CREATE TABLE instructores (
    ci VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL
);


CREATE TABLE alumnos (
    ci VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(255)
);

CREATE TABLE clase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ci_instructor VARCHAR(20),
    id_actividad INT,
    id_turno INT,
    dictada BOOLEAN NOT NULL,
    turno ENUM('De 9:00 a 11:00', 'De 12:00 a 14:00', 'De 16:00 a 18:00') NOT NULL,
    tipo_actividad ENUM('grupal', 'individual') NOT NULL,
    FOREIGN KEY (ci_instructor) REFERENCES instructores(ci),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id)
);

CREATE TABLE alumno_clase (
    id_clase INT,
    ci_alumno VARCHAR(20),
    id_equipamiento INT,
    PRIMARY KEY (id_clase, ci_alumno),
    FOREIGN KEY (id_clase) REFERENCES clase(id),
    FOREIGN KEY (ci_alumno) REFERENCES alumnos(ci),
    FOREIGN KEY (id_equipamiento) REFERENCES equipamiento(id)
);

SHOW TABLES;