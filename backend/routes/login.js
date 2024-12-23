const express = require('express');
const router = express.Router();
const mysql = require('mysql');
const bcrypt = require('bcrypt');
const crypto = require('crypto');

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

function createSessionToken() {
  return crypto.randomBytes(16).toString('hex');
}

router.post('/', (req, res) => {
  const { username, password } = req.body;

  console.log(`Intentando iniciar sesi  n con username: ${username}`);

  db.query('SELECT * FROM usuarios WHERE nombre = ? OR correo = ?', [username, username], (err, userResults) => {
    if (err) {
      console.error('Error en la base de datos al buscar usuario:', err);
      return res.json({ success: false, message: 'Error en la base de datos.' });
    }

    if (userResults.length > 0) {
      const user = userResults[0];
      bcrypt.compare(password, user.hash_password, (err, isMatch) => {
        if (err) {
          console.error('Error comparando contrase  as:', err);
          return res.json({ success: false, message: 'Error en la comparaci  n de contrase  as.' });
        }

        if (!isMatch) {
          return res.json({ success: false, message: 'Contrase  a incorrecta.' });
        }

        const sessionToken = createSessionToken();
        res.cookie('session_token', sessionToken, { httpOnly: true, secure: false }); // Aseg  rate de que la cookie se est   configurando correctamente

        db.query('INSERT INTO sessions (user_id, token) VALUES (?, ?)', [user.id, sessionToken], (err, results) => {
          if (err) {
            console.error('Error al guardar el token de sesi  n en la base de datos:', err);
            return res.json({ success: false, message: 'Error en la base de datos.' });
          }
          return res.json({ success: true, user_id: user.id, role: user.rol });
        });
      });
    } else {
      return res.json({ success: false, message: 'Usuario no encontrado.' });
    }
  });
});

module.exports = router;

