const express = require('express');
const router = express.Router();
const mysql = require('mysql');
const verifySession = require('../middleware/auth');

const db = mysql.createConnection({
  host: 'db',
  user: 'root',
  password: 'contrasena',
  database: 'permisos'
});

db.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the permisos database.');
});

router.use(verifySession);  // Aplicar el middleware de verificaci  n de sesi  n

router.get('/:id', (req, res) => {
  const userId = req.params.id;

  console.log(`Obteniendo datos para el usuario con ID: ${userId}`);

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
    console.log('Datos del usuario:', user);

    return res.json({ success: true, user });
  });
});

module.exports = router;




