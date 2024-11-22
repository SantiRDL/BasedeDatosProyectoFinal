import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Inscripciones() {
const [inscripciones, setInscripciones] = useState([]);
const [idClase, setIdClase] = useState('');
const [ciAlumno, setCiAlumno] = useState('');
const [idEquipamiento, setIdEquipamiento] = useState('');

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

const handleSubmit = async (event) => {
    event.preventDefault();
    try {
    await axios.post('http://localhost:5000/inscripciones', {
        id_clase: idClase,
        ci_alumno: ciAlumno,
        id_equipamiento: idEquipamiento,
    });
    fetchInscripciones();
    resetForm();
    } catch (error) {
    console.error('Error adding inscripcion', error);
    }
};

const resetForm = () => {
    setIdClase('');
    setCiAlumno('');
    setIdEquipamiento('');
};

return (
    <div className="Inscripciones">
    <h2>Inscripciones</h2>
    <form onSubmit={handleSubmit}>
        <div>
        <label htmlFor="idClase">ID Clase:</label>
        <input
            type="text"
            id="idClase"
            value={idClase}
            onChange={(e) => setIdClase(e.target.value)}
            required
        />
        </div>
        <div>
        <label htmlFor="ciAlumno">CI Alumno:</label>
        <input
            type="text"
            id="ciAlumno"
            value={ciAlumno}
            onChange={(e) => setCiAlumno(e.target.value)}
            required
        />
        </div>
        <div>
        <label htmlFor="idEquipamiento">ID Equipamiento:</label>
        <input
            type="text"
            id="idEquipamiento"
            value={idEquipamiento}
            onChange={(e) => setIdEquipamiento(e.target.value)}
            required
        />
        </div>
        <button type="submit">Inscribir</button>
    </form>
    <h3>Lista de Inscripciones</h3>
    <ul>
        {inscripciones.map((inscripcion, index) => (
        <li key={index}>
            Clase: {inscripcion.descripcion_clase}, Alumno: {inscripcion.nombre_alumno} {inscripcion.apellido_alumno}, Equipamiento: {inscripcion.descripcion_equipamiento}
        </li>
        ))}
    </ul>
    </div>
);
}

export default Inscripciones;