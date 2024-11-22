import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AdmInstructores() {
const [instructores, setInstructores] = useState([]);
const [ci, setCi] = useState('');
const [nombre, setNombre] = useState('');
const [apellido, setApellido] = useState('');
const [editMode, setEditMode] = useState(false);

useEffect(() => {
    fetchInstructores();
}, []);

const fetchInstructores = async () => {
    try {
    const response = await axios.get('http://localhost:5000/instructores');
    setInstructores(response.data);
    } catch (error) {
    console.error('Error fetching instructores', error);
    }
};

const handleSubmit = async (event) => {
    event.preventDefault();
    if (editMode) {
    await axios.put(`http://localhost:5000/instructores/${ci}`, { nombre, apellido });
    } else {
    await axios.post('http://localhost:5000/instructores', { ci, nombre, apellido });
    }
    fetchInstructores();
    resetForm();
};

const handleEdit = (instructor) => {
    setCi(instructor.ci);
    setNombre(instructor.nombre);
    setApellido(instructor.apellido);
    setEditMode(true);
};

const handleDelete = async (ci) => {
    await axios.delete(`http://localhost:5000/instructores/${ci}`);
    fetchInstructores();
};

const resetForm = () => {
    setCi('');
    setNombre('');
    setApellido('');
    setEditMode(false);
};

return (
    <div className="AdmInstructores">
    <h2>Administrar Instructores</h2>
    <form onSubmit={handleSubmit}>
        <div>
        <label htmlFor="ci">CI:</label>
        <input
            type="text"
            id="ci"
            value={ci}
            onChange={(e) => setCi(e.target.value)}
            required
            disabled={editMode}
        />
        </div>
        <div>
            <label htmlFor="nombre">Nombre:</label>
            <input
                type="text"
                id="nombre"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
                required
            />
        </div>
        <div>
            <label htmlFor="apellido">Apellido:</label>
            <input
                type="text"
                id="apellido"
                value={apellido}
                onChange={(e) => setApellido(e.target.value)}
                required
            />
        </div>
        <button type="submit">{editMode ? 'Modificar' : 'Agregar'}</button>
        {editMode && <button type="button" onClick={resetForm}>Cancelar</button>}
    </form>
    <h3>Lista de Instructores</h3>
    <ul>
        {instructores.map((instructor) => (
        <li key={instructor.ci}>
            {instructor.nombre} {instructor.apellido}
            <button onClick={() => handleEdit(instructor)}>Editar</button>
            <button onClick={() => handleDelete(instructor.ci)}>Eliminar</button>
        </li>
        ))}
    </ul>
    </div>
);
}

export default AdmInstructores;