import React, { useState, useEffect } from "react";
import "./Styles/ActivityManagement.css";
import { fetchActivities, createActivity } from "../services/api";

function ActivityManagement() {
  const [activities, setActivities] = useState([]);
  const [newActivity, setNewActivity] = useState({ description: "", cost: "" });

  useEffect(() => {
    fetchActivities().then(data => setActivities(data));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    createActivity(newActivity).then(() => {
      alert("Actividad creada.");
      fetchActivities().then(data => setActivities(data));
    });
  };

  return (
    <div>
      <h1>Gestión de Actividades</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Descripción"
          value={newActivity.description}
          onChange={(e) => setNewActivity({ ...newActivity, description: e.target.value })}
        />
        <input
          type="number"
          placeholder="Costo"
          value={newActivity.cost}
          onChange={(e) => setNewActivity({ ...newActivity, cost: e.target.value })}
        />
        <button type="submit">Agregar Actividad</button>
      </form>
      <ul>
        {activities.map((activity, index) => (
          <li key={index}>{`${activity.description} - $${activity.cost}`}</li>
        ))}
      </ul>
    </div>
  );
}

export default ActivityManagement;
