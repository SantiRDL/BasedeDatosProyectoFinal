import React, { useState, useEffect } from "react";
import "./Styles/StudentManagement.css";
import { fetchStudents, createStudent } from "../services/api";

function StudentManagement() {
  const [students, setStudents] = useState([]);
  const [newStudent, setNewStudent] = useState({
    ci: "",
    name: "",
    surname: "",
    birthdate: "",
    email: "",
    phone: ""
  });

  useEffect(() => {
    fetchStudents().then(data => setStudents(data));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    createStudent(newStudent).then(() => {
      alert("Alumno creado.");
      fetchStudents().then(data => setStudents(data));
    });
  };

  return (
    <div>
      <h1>Gestión de Alumnos</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Cédula"
          value={newStudent.ci}
          onChange={(e) => setNewStudent({ ...newStudent, ci: e.target.value })}
        />
        <input
          type="text"
          placeholder="Nombre"
          value={newStudent.name}
          onChange={(e) => setNewStudent({ ...newStudent, name: e.target.value })}
        />
        <input
          type="text"
          placeholder="Apellido"
          value={newStudent.surname}
          onChange={(e) => setNewStudent({ ...newStudent, surname: e.target.value })}
        />
        <input
          type="date"
          placeholder="Fecha de nacimiento"
          value={newStudent.birthdate}
          onChange={(e) => setNewStudent({ ...newStudent, birthdate: e.target.value })}
        />
        <input
          type="email"
          placeholder="Correo electrónico"
          value={newStudent.email}
          onChange={(e) => setNewStudent({ ...newStudent, email: e.target.value })}
        />
        <input
          type="text"
          placeholder="Teléfono"
          value={newStudent.phone}
          onChange={(e) => setNewStudent({ ...newStudent, phone: e.target.value })}
        />
        <button type="submit">Agregar Alumno</button>
      </form>
      <ul>
        {students.map((student, index) => (
          <li key={index}>{`${student.name} ${student.surname} (${student.ci})`}</li>
        ))}
      </ul>
    </div>
  );
}

export default StudentManagement;
