import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AdmTurnos() {
const [turnos, setTurnos] = useState([]);
const [id, setId] = useState('');
const [descripcion, setDescripcion] = useState('');
const [editMode, setEditMode] = useState(false);

useEffect(() => {
    fetchTurnos();
}, []);

const fetchTurnos = async () => {
    try {
    const response = await axios.get('http://localhost:5000/turnos');
    setTurnos(response.data);
    } catch (error) {
    console.error('Error fetching turnos', error);
    }
};

const handleSubmit = async (event) => {
    event.preventDefault();
    if (editMode) {
    await axios.put(`http://localhost:5000/turnos/${id}`, { descripcion });
    } else {
    await axios.post('http://localhost:5000/turnos', { descripcion });
    }
    fetchTurnos();
    resetForm();
};

const handleEdit = (turno) => {
    setId(turno.id);
    setDescripcion(turno.descripcion);
    setEditMode(true);
};

const handleDelete = async (id) => {
    await axios.delete(`http://localhost:5000/turnos/${id}`);
    fetchTurnos();
};

const resetForm = () => {
    setId('');
    setDescripcion('');
    setEditMode(false);
};

return (
    <div className="AdmTurnos">
    <h2>Administrar Turnos</h2>
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
        <button type="submit">{editMode ? 'Modificar' : 'Agregar'}</button>
        {editMode && <button type="button" onClick={resetForm}>Cancelar</button>}
    </form>
    <h3>Lista de Turnos</h3>
    <ul>
        {turnos.map((turno) => (
        <li key={turno.id}>
            {turno.descripcion}
            <button onClick={() => handleEdit(turno)}>Editar</button>
            <button onClick={() => handleDelete(turno.id)}>Eliminar</button>
        </li>
        ))}
    </ul>
    </div>
);
}

export default AdmTurnos;