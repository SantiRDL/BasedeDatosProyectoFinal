import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Reportes() {
  const [actividadesIngresos, setActividadesIngresos] = useState([]);
  const [actividadesAlumnos, setActividadesAlumnos] = useState([]);
  const [turnosClases, setTurnosClases] = useState([]);

  useEffect(() => {
    fetchActividadesIngresos();
    fetchActividadesAlumnos();
    fetchTurnosClases();
  }, []);

  const fetchActividadesIngresos = async () => {
    try {
      const response = await axios.get('http://localhost:5000/reportes/actividades_ingresos');
      setActividadesIngresos(response.data);
    } catch (error) {
      console.error('Error fetching actividades ingresos', error);
    }
  };

  const fetchActividadesAlumnos = async () => {
    try {
      const response = await axios.get('http://localhost:5000/reportes/actividades_alumnos');
      setActividadesAlumnos(response.data);
    } catch (error) {
      console.error('Error fetching actividades alumnos', error);
    }
  };

  const fetchTurnosClases = async () => {
    try {
      const response = await axios.get('http://localhost:5000/reportes/turnos_clases');
      setTurnosClases(response.data);
    } catch (error) {
      console.error('Error fetching turnos clases', error);
    }
  };

  return (
    <div className="Reportes">
      <h2>Reportes</h2>
      <h3>Actividades que más ingresos generan</h3>
      <ul>
        {actividadesIngresos.map((actividad, index) => (
          <li key={index}>
            {actividad.descripcion}: ${actividad.total_ingresos}
          </li>
        ))}
      </ul>
      <h3>Actividades con más alumnos</h3>
      <ul>
        {actividadesAlumnos.map((actividad, index) => (
          <li key={index}>
            {actividad.descripcion}: {actividad.total_alumnos} alumnos
          </li>
        ))}
      </ul>
      <h3>Turnos con más clases dictadas</h3>
      <ul>
        {turnosClases.map((turno, index) => (
          <li key={index}>
            {turno.descripcion}: {turno.total_clases} clases
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Reportes;