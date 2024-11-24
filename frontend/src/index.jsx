import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App"; // Importa el componente raíz
import "./index.css"; // Estilos globales

// Obtén el elemento raíz en el DOM donde se montará la aplicación
const root = ReactDOM.createRoot(document.getElementById("root"));

// Renderiza la aplicación
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
