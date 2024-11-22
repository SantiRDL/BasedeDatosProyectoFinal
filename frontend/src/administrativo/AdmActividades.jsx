import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AdmActividades() {
const [actividades, setActividades] = useState([]);
const [id, setId] = useState('');
const [descripcion, setDescripcion] = useState('');
const [costo, setCosto] = useState('');
const [instructor, setInstructor] = useState('');
const [turno, setTurno] = useState('');
const [editMode, setEditMode] = useState(false);

useEffect(() => {
    fetchActividades();
}, []);

const fetchActividades = async () => {
    try {
    const response = await axios.get('http://localhost:5000/actividades');
    setActividades(response.data);
    } catch (error) {
    console.error('Error fetching actividades', error);
    }
};

const handleSubmit = async (event) => {
    event.preventDefault();
    if (editMode) {
    await axios.put(`http://localhost:5000/actividades/${id}`, { descripcion, costo, instructor, turno });
    } else {
    await axios.post('http://localhost:5000/actividades', { descripcion, costo, instructor, turno });
    }
    fetchActividades();
    resetForm();
};

const handleEdit = (actividad) => {
    setId(actividad.id);
    setDescripcion(actividad.descripcion);
    setCosto(actividad.costo);
    setInstructor(actividad.instructor);
    setTurno(actividad.turno);
    setEditMode(true);
};

const resetForm = () => {
    setId('');
    setDescripcion('');
    setCosto('');
    setInstructor('');
    setTurno('');
    setEditMode(false);
};

return (
    <div className="AdmActividades">
    <h2>Administrar Actividades</h2>
    <form onSubmit={handleSubmit}>
        <div>
        <label htmlFor="descripcion">Descripción:</label>
        <input
            type="text"
            id="descripcion"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
            required
        />
        </div>
        <div>
        <label htmlFor="costo">Costo:</label>
        <input
            type="number"
            id="costo"
            value={costo}
            onChange={(e) => setCosto(e.target.value)}
            required
        />
        </div>
        <div>
        <label htmlFor="instructor">Instructor:</label>
        <input
            type="text"
            id="instructor"
            value={instructor}
            onChange={(e) => setInstructor(e.target.value)}
        />
        </div>
        <div>
        <label htmlFor="turno">Turno:</label>
        <input
            type="text"
            id="turno"
            value={turno}
            onChange={(e) => setTurno(e.target.value)}
        />
        </div>
        <button type="submit">{editMode ? 'Modificar' : 'Agregar'}</button>
        {editMode && <button type="button" onClick={resetForm}>Cancelar</button>}
    </form>
    <h3>Lista de Actividades</h3>
    <ul>
        {actividades.map((actividad) => (
        <li key={actividad.id}>
            {actividad.descripcion} - {actividad.costo} - {actividad.instructor} - {actividad.turno}
            <button onClick={() => handleEdit(actividad)}>Editar</button>
        </li>
        ))}
    </ul>
    </div>
);
}

export default AdmActividades;