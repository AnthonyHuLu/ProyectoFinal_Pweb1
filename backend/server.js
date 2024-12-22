const express = require('express');
const cors = require('cors');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());
app.use(bodyParser.json());
app.use(cookieParser()); // Agrega este middleware

const dbPrincipal = mysql.createConnection({
  host: 'db',
  user: 'root',
  password: 'contrasena',
  database: 'principal'
});

dbPrincipal.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the principal database.');
});

// Ruta para manejar el registro de mascotas
const registroMascotaRoute = require('./routes/registro_mascota');
app.use('/registro_mascota', registroMascotaRoute);

// Ruta para el inicio de sesión
const loginRoute = require('./routes/login');
app.use('/api/login', loginRoute);

// Ruta para manejar los datos del usuario
const userRoute = require('./routes/user');
app.use('/api/user', userRoute);

// Ruta para manejar el cierre de sesión
const logoutRoute = require('./routes/logout');
app.use('/api/logout', logoutRoute);

// Otras rutas de la API...

app.get('/api/productos', (req, res) => {
  const query = 'SELECT * FROM productos';
  dbPrincipal.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching products:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

app.get('/api/publicaciones', (req, res) => {
  const query = 'SELECT * FROM publicaciones';
  dbPrincipal.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching publications:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

app.get('/api/perfiles', (req, res) => {
  const query = 'SELECT * FROM perfiles';
  dbPrincipal.query(query, (err, results) => {
    if (err) {
      console.error('Error fetching profiles:', err);
      res.status(500).send('Internal Server Error');
      return;
    }
    res.json(results);
  });
});

app.get('/api/fotos', (req, res) => {
  const query = 'SELECT * FROM fotos';
  dbPrincipal.query(query, (err, results) => {
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

