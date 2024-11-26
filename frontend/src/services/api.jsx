const BASE_URL = "http://localhost:5000/api";

// --- Instructores ---
export const fetchInstructors = async () => {
  const response = await fetch(`${BASE_URL}/instructors`, {
    method: "GET",
  });
  
  if (!response.ok) {
    throw new Error("Error al obtener instructores");
  }
  return await response.json();
};

export const createInstructor = async (instructor) => {
  await fetch(`${BASE_URL}/instructors`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(instructor),
  });
};

export const updateInstructor = async (id, instructor) => {
  await fetch(`${BASE_URL}/instructors/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(instructor),
  });
};

export const deleteInstructor = async (id) => {
  await fetch(`${BASE_URL}/instructors/${id}`, {
    method: "DELETE",
  });
};

// --- Actividades ---
export const fetchActivities = async () => {
  const response = await fetch(`${BASE_URL}/activities`);
  return await response.json();
};

export const createActivity = async (activity) => {
  await fetch(`${BASE_URL}/activities`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(activity),
  });
};

export const updateActivity = async (id, activity) => {
  await fetch(`${BASE_URL}/activities/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(activity),
  });
};

export const deleteActivity = async (id) => {
  await fetch(`${BASE_URL}/activities/${id}`, {
    method: "DELETE",
  });
};

// --- Alumnos ---
export const fetchStudents = async () => {
  const response = await fetch(`${BASE_URL}/students`);
  return await response.json();
};

export const createStudent = async (student) => {
  await fetch(`${BASE_URL}/students`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(student),
  });
};

export const updateStudent = async (ci, student) => {
  await fetch(`${BASE_URL}/students/${ci}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(student),
  });
};

export const deleteStudent = async (ci) => {
  await fetch(`${BASE_URL}/students/${ci}`, {
    method: "DELETE",
  });
};

// --- Clases ---
export const fetchClasses = async () => {
  const response = await fetch(`${BASE_URL}/classes`);
  return await response.json();
};

export const createClass = async (classData) => {
  await fetch(`${BASE_URL}/classes`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(classData),
  });
};

export const updateClass = async (id, classData) => {
  await fetch(`${BASE_URL}/classes/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(classData),
  });
};

export const deleteClass = async (id) => {
  await fetch(`${BASE_URL}/classes/${id}`, {
    method: "DELETE",
  });
};
