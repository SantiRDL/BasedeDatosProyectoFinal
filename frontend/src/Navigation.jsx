import React from 'react';
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <div>
      <h1>Administración</h1>
      <nav>
        <ul>
          <li>
            <Link to="/instructores">Administrar Instructores</Link>
          </li>
          <li>
            <Link to="/actividades">Administrar Actividades</Link>
          </li>
          <li>
            <Link to="/alumnos">Administrar Alumnos</Link>
          </li>
          <li>
            <Link to="/turnos">Administrar Turnos</Link>
          </li>
          <li>
            <Link to="/inscripciones">Inscripciones</Link>
          </li>
          <li>
            <Link to="/mis-clases">Mis Clases</Link>
          </li>
          <li>
            <Link to="/clases">Clases Disponibles</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Navigation;