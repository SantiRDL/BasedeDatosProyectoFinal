import React, { useState, useEffect } from "react";
import "./Styles/ClassManagement.css";
import { fetchClasses, createClass } from "../services/api";

function ClassManagement() {
  const [classes, setClasses] = useState([]);
  const [newClass, setNewClass] = useState({ instructorId: "", activityId: "", turnId: "" });

  useEffect(() => {
    fetchClasses().then(data => setClasses(data));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    createClass(newClass).then(() => {
      alert("Clase creada.");
      fetchClasses().then(data => setClasses(data));
    });
  };

  return (
    <div>
      <h1>Gestión de Clases</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="ID del Instructor"
          value={newClass.instructorId}
          onChange={(e) => setNewClass({ ...newClass, instructorId: e.target.value })}
        />
        <input
          type="text"
          placeholder="ID de la Actividad"
          value={newClass.activityId}
          onChange={(e) => setNewClass({ ...newClass, activityId: e.target.value })}
        />
        <input
          type="text"
          placeholder="ID del Turno"
          value={newClass.turnId}
          onChange={(e) => setNewClass({ ...newClass, turnId: e.target.value })}
        />
        <button type="submit">Agregar Clase</button>
      </form>
      <ul>
        {classes.map((cl, index) => (
          <li key={index}>{`Clase ${cl.id} - Instructor: ${cl.instructorId} - Actividad: ${cl.activityId}`}</li>
        ))}
      </ul>
    </div>
  );
}

export default ClassManagement;
