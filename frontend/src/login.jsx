import React, { useState } from 'react';
import axios from 'axios';

function Login() {
    const [correo, setCorreo] = useState('');
    const [contraseña, setContraseña] = useState('');
    const [mensaje, setMensaje] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
        const response = await axios.post('http://localhost:5000/login', {
            correo,
            contraseña,
            });
        setMensaje(response.data.message);
        }   catch (error) {
            setMensaje('Error al iniciar sesión');
        }
    };

    return (
        <div className="Login">
            <form onSubmit={handleSubmit}>
            <div>
            <label htmlFor="correo">Correo:</label>
            <input
                type="email"
                id="correo"
                value={correo}
                onChange={(e) => setCorreo(e.target.value)}
                required
            />
        </div>
        <div>
            <label htmlFor="contraseña">Contraseña:</label>
            <input
                type="password"
                id="contraseña"
                value={contraseña}
                onChange={(e) => setContraseña(e.target.value)}
                required
            />
        </div>
        <button type="submit">Iniciar sesión</button>
        </form>
        {mensaje && <p>{mensaje}</p>}
        </div>
    );
}

export default Login;