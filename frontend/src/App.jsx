import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Dashboard from "./components/Dashboard";
import InstructorManagement from "./components/InstructorManagement";
import ActivityManagement from "./components/ActivityManagement";
import StudentManagement from "./components/StudentManagement";
import ClassManagement from "./components/ClassManagement";
import Reports from "./components/Reports";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/instructors" element={<InstructorManagement />} />
        <Route path="/activities" element={<ActivityManagement />} />
        <Route path="/students" element={<StudentManagement />} />
        <Route path="/classes" element={<ClassManagement />} />
        <Route path="/reports" element={<Reports />} />
      </Routes>
    </Router>
  );
}

export default App;
