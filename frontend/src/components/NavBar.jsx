import React from "react";
import "./Styles/NavBar.css";
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <nav>
      <ul>
        <li><Link to="/">Dashboard</Link></li>
        <li><Link to="/instructors">Instructores</Link></li>
        <li><Link to="/activities">Actividades</Link></li>
        <li><Link to="/students">Alumnos</Link></li>
        <li><Link to="/classes">Clases</Link></li>
        <li><Link to="/reports">Reportes</Link></li>
      </ul>
    </nav>
  );
}

export default NavBar;
