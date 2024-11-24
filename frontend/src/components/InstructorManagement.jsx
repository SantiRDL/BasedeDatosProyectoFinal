import React, { useState, useEffect } from "react";
import "./Styles/InstructorManagement.css";
import { fetchInstructors, createInstructor } from "../services/api";

function InstructorManagement() {
  const [instructors, setInstructors] = useState([]);
  const [newInstructor, setNewInstructor] = useState({ name: "", surname: "" });

  useEffect(() => {
    fetchInstructors().then(data => setInstructors(data));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    createInstructor(newInstructor).then(() => {
      alert("Instructor creado.");
      fetchInstructors().then(data => setInstructors(data));
    });
  };

  return (
    <div className="management-container">
      <h1>Gestión de Instructores</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Nombre"
          value={newInstructor.name}
          onChange={(e) => setNewInstructor({ ...newInstructor, name: e.target.value })}
        />
        <input
          type="text"
          placeholder="Apellido"
          value={newInstructor.surname}
          onChange={(e) => setNewInstructor({ ...newInstructor, surname: e.target.value })}
        />
        <button type="submit">Agregar Instructor</button>
      </form>
      <ul>
        {instructors.map((instructor, index) => (
          <li key={index}>
            <span>{`${instructor.name} ${instructor.surname}`}</span>
            <button className="delete-button">Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default InstructorManagement;
