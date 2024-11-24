import React from "react";
import "./Styles/Dashboard.css"; // Archivo de estilos opcional para estilos específicos

function Dashboard() {
  return (
    <div className="dashboard-container">
      <h1>Dashboard</h1>
      <p>Bienvenido al sistema administrativo de la escuela de deportes de nieve.</p>
      <div className="dashboard-summary">
        <p>Desde aquí puedes gestionar instructores, actividades, alumnos y clases.</p>
      </div>
    </div>
  );
}

export default Dashboard;
