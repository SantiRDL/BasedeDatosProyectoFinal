import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AdmAlumnos() {
const [alumnos, setAlumnos] = useState([]);
const [id, setId] = useState('');
const [nombre, setNombre] = useState('');
const [ci, setCi] = useState('');
const [apellido, setApellido] = useState('');
const [fechaNacimiento, setFechaNacimiento] = useState('');
const [telefono, setTelefono] = useState('');
const [correo, setCorreo] = useState('');
const [editMode, setEditMode] = useState(false);

useEffect(() => {
    fetchAlumnos();
}, []);

const fetchAlumnos = async () => {
    try {
        const response = await axios.get('http://localhost:5000/alumnos');
        setAlumnos(response.data);
    } catch (error) {
        console.error('Error fetching alumnos', error);
    }
};

const handleSubmit = async (event) => {
    event.preventDefault();
    if (editMode) {
        await axios.put(`http://localhost:5000/alumnos/${id}`, { nombre, ci, apellido, fecha_nacimiento: fechaNacimiento, telefono, correo });
    } else {
        await axios.post('http://localhost:5000/alumnos', { nombre, ci, apellido, fecha_nacimiento: fechaNacimiento, telefono, correo });
    }
    fetchAlumnos();
    resetForm();
};

const handleEdit = (alumno) => {
    setId(alumno.id);
    setNombre(alumno.nombre);
    setCi(alumno.ci);
    setApellido(alumno.apellido);
    setFechaNacimiento(alumno.fecha_nacimiento);
    setTelefono(alumno.telefono);
    setCorreo(alumno.correo);
    setEditMode(true);
};

const handleDelete = async (id) => {
    await axios.delete(`http://localhost:5000/alumnos/${id}`);
    fetchAlumnos();
};

const resetForm = () => {
    setId('');
    setNombre('');
    setCi('');
    setApellido('');
    setFechaNacimiento('');
    setTelefono('');
    setCorreo('');
    setEditMode(false);
};

return (
    <div className="AdmAlumnos">
    <h2>Administrar Alumnos</h2>
    <form onSubmit={handleSubmit}>
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
        <label htmlFor="ci">CI:</label>
        <input
            type="text"
            id="ci"
            value={ci}
            onChange={(e) => setCi(e.target.value)}
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
        <div>
        <label htmlFor="fechaNacimiento">Fecha de Nacimiento:</label>
        <input
            type="date"
            id="fechaNacimiento"
            value={fechaNacimiento}
            onChange={(e) => setFechaNacimiento(e.target.value)}
            required
        />
        </div>
        <div>
        <label htmlFor="telefono">Teléfono:</label>
        <input
            type="text"
            id="telefono"
            value={telefono}
            onChange={(e) => setTelefono(e.target.value)}
        />
        </div>
        <div>
        <label htmlFor="correo">Correo:</label>
        <input
            type="email"
            id="correo"
            value={correo}
            onChange={(e) => setCorreo(e.target.value)}
        />
        </div>
        <button type="submit">{editMode ? 'Modificar' : 'Agregar'}</button>
        {editMode && <button type="button" onClick={resetForm}>Cancelar</button>}
    </form>
    <h3>Lista de Alumnos</h3>
    <ul>
        {alumnos.map((alumno) => (
        <li key={alumno.id}>
            {alumno.nombre} {alumno.apellido} - {alumno.ci}
            <button onClick={() => handleEdit(alumno)}>Editar</button>
            <button onClick={() => handleDelete(alumno.id)}>Eliminar</button>
        </li>
        ))}
    </ul>
    </div>
);
}

export default AdmAlumnos;