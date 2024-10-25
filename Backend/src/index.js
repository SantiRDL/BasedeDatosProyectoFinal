const express = require('express');
const cors = require('cors');
const db = require('./database');

const app = express();
app.use(cors());
app.use(express.json());

// Ruta para obtener datos
app.get('/api/items', (req, res) => {
  db.query('SELECT * FROM items', (err, results) => {
    if (err) return res.status(500).json({ error: err });
    res.json(results);
  });
});

// Ruta para agregar datos
app.post('/api/items', (req, res) => {
  const { name } = req.body;
  db.query('INSERT INTO items (name) VALUES (?)', [name], (err, result) => {
    if (err) return res.status(500).json({ error: err });
    res.json({ message: 'Item added', id: result.insertId });
  });
});

// Iniciar el servidor
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
