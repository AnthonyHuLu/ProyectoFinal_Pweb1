const express = require('express');
const router = express.Router();
const mysql = require('mysql');
const verifySession = require('../middleware/auth');

const db = mysql.createConnection({
  host: 'db',
  user: 'root',
  password: 'contrasena',
  database: 'permisos' // Conectar a la base de datos 'permisos'
});

db.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the permisos database.');
});

// Usar el middleware para verificar la sesión
router.use(verifySession);

// Ruta para obtener los datos del usuario incluyendo sus mascotas
router.get('/:id', (req, res) => {
  const userId = req.params.id;

  db.query('SELECT * FROM usuarios WHERE id = ?', [userId], (err, userResults) => {
    if (err) {
      console.error('Error en la consulta de usuarios:', err);
      return res.json({ success: false, message: 'Error en la base de datos.' });
    }

    if (userResults.length === 0) {
      console.log('Usuario no encontrado.');
      return res.json({ success: false, message: 'Usuario no encontrado.' });
    }

    const user = userResults[0];

    db.query('SELECT * FROM mascotas WHERE duenio_id = ?', [userId], (err, petResults) => {
      if (err) {
        console.error('Error en la consulta de mascotas:', err);
        return res.json({ success: false, message: 'Error en la base de datos al obtener mascotas.' });
      }

      console.log('Datos del usuario:', user);
      console.log('Mascotas del usuario:', petResults);

      return res.json({ success: true, user, mascotas: petResults });
    });
  });
});

module.exports = router;

