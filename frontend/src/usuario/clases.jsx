import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Clases() {
const [clases, setClases] = useState([]);

useEffect(() => {
    fetchClases();
}, []);

const fetchClases = async () => {
    try {
    const response = await axios.get('http://localhost:5000/clases');
    setClases(response.data);
    } catch (error) {
    console.error('Error fetching clases', error);
    }
};

return (
    <div className="Clases">
    <h2>Lista de Clases Disponibles</h2>
    <ul>
        {clases.map((clase) => (
        <li key={clase.id}>
            <h3>{clase.descripcion}</h3>
            <p>Instructor: {clase.instructor}</p>
            <p>Turno: {clase.turno}</p>
            <p>Costo: {clase.costo}</p>
        </li>
        ))}
    </ul>
    </div>
);
}

export default Clases;