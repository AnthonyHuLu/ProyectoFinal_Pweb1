const express = require('express');
const cors = require('cors');
const mysql = require('mysql');

const app = express();
const port = 3000;

app.use(cors());

const db = mysql.createConnection({
  host: 'db', // Nombre del servicio del contenedor MariaDB en Docker Compose
  user: 'root',
  password: 'contrasena',
  database: 'principal'
});

db.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the database.');
});

// Rutas de la API...

// Ruta para obtener productos
app.get('/api/productos', (req, res) => {
  const query = 'SELECT * FROM productos';
  db.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching products:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

// Ruta para obtener publicaciones
app.get('/api/publicaciones', (req, res) => {
  const query = 'SELECT * FROM publicaciones';
  db.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching publications:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

// Ruta para obtener perfiles
app.get('/api/perfiles', (req, res) => {
  const query = 'SELECT * FROM perfiles';
  db.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching profiles:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

// Ruta para obtener fotos
app.get('/api/fotos', (req, res) => {
  const query = 'SELECT * FROM fotos';
  db.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching photos:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

// Ruta para obtener likes de foros
app.get('/api/likes_foros', (req, res) => {
  const query = 'SELECT * FROM likes_foros';
  db.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching likes:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

// Ruta para obtener tipos de cliente
app.get('/api/tipos_cliente', (req, res) => {
  const query = 'SELECT * FROM tipos_cliente';
  db.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching client types:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

// Ruta para obtener pedidos
app.get('/api/pedidos', (req, res) => {
  const query = 'SELECT * FROM pedidos';
  db.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching orders:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

