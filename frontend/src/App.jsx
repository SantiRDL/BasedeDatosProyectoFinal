import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import Login from './login';
import './App.css';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  );
}

export default App;
