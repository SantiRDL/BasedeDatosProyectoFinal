import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Misclases() {
  const [inscripciones, setInscripciones] = useState([]);

  useEffect(() => {
    fetchInscripciones();
  }, []);

  const fetchInscripciones = async () => {
    try {
      const response = await axios.get('http://localhost:5000/inscripciones');
      setInscripciones(response.data);
    } catch (error) {
      console.error('Error fetching inscripciones', error);
    }
  };

  return (
    <div className="Misclases">
      <h2>Mis Clases</h2>
      <ul>
        {inscripciones.map((inscripcion, index) => (
          <li key={index}>
            Clase: {inscripcion.descripcion_clase}, Instructor: {inscripcion.instructor}, Turno: {inscripcion.turno}, Equipamiento: {inscripcion.descripcion_equipamiento}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Misclases;