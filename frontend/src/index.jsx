import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AdmInstructores from './administrativo/AdmInstructores';
import AdmActividades from './administrativo/AdmActividades';
import AdmAlumnos from './administrativo/AdmAlumnos';
import AdmTurnos from './administrativo/AdmTurnos';
import Navigation from './Navigation';
import Inscripciones from './usuario/Inscripciones';
import MisClases from './usuario/Misclases';
import Clases from './usuario/clases';
import Reportes from './Reportes';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Navigation />
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/instructores" element={<AdmInstructores />} />
        <Route path="/actividades" element={<AdmActividades />} />
        <Route path="/alumnos" element={<AdmAlumnos />} />
        <Route path="/turnos" element={<AdmTurnos />} />
        <Route path="/inscripciones" element={<Inscripciones />} />
        <Route path="/mis-clases" element={<MisClases />} />
        <Route path="/clases" element={<Clases />} />
        <Route path="/reportes" element={<Reportes />} />
      </Routes>
    </Router>
  </React.StrictMode>
);

reportWebVitals();
