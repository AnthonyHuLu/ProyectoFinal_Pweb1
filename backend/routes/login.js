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

  console.log(`Intentando iniciar sesión con username: ${username}`);

  db.query('SELECT * FROM usuarios WHERE nombre = ? OR correo = ?', [username, username], (err, userResults) => {
    if (err) {
      console.error('Error en la base de datos al buscar usuario:', err);
      return res.json({ success: false, message: 'Error en la base de datos.' });
    }

    if (userResults.length > 0) {
      console.log('Usuario encontrado:', userResults[0]);
      const user = userResults[0];
      bcrypt.compare(password, user.hash_password, (err, isMatch) => {
        if (err) {
          console.error('Error comparando contraseñas:', err);
          return res.json({ success: false, message: 'Error en la comparación de contraseñas.' });
        }

        if (!isMatch) {
          return res.json({ success: false, message: 'Contraseña incorrecta.' });
        }

        const sessionToken = createSessionToken();
        res.cookie('session_token', sessionToken, { httpOnly: true, secure: false });

        db.query('INSERT INTO sessions (user_id, token) VALUES (?, ?)', [user.id, sessionToken], (err, results) => {
          if (err) {
            console.error('Error al guardar el token de sesión en la base de datos:', err);
            return res.json({ success: false, message: 'Error en la base de datos.' });
          }
          return res.json({ success: true, user_id: user.id, role: user.rol });
        });
      });
    } else {
      db.query('SELECT * FROM mascotas WHERE nombre = ?', [username], (err, petResults) => {
        if (err) {
          console.error('Error en la base de datos al buscar mascota:', err);
          return res.json({ success: false, message: 'Error en la base de datos.' });
        }

        if (petResults.length > 0) {
          console.log('Mascota encontrada:', petResults[0]);
          const pet = petResults[0];
          db.query('SELECT * FROM usuarios WHERE id = ?', [pet.duenio_id], (err, ownerResults) => {
            if (err) {
              console.error('Error en la base de datos al buscar dueño:', err);
              return res.json({ success: false, message: 'Error en la base de datos.' });
            }

            if (ownerResults.length === 0) {
              console.log('Dueño no encontrado.');
              return res.json({ success: false, message: 'Dueño no encontrado.' });
            }

            console.log('Dueño encontrado:', ownerResults[0]);
            const owner = ownerResults[0];
            bcrypt.compare(password, owner.hash_password, (err, isMatch) => {
              if (err) {
                console.error('Error comparando contraseñas:', err);
                return res.json({ success: false, message: 'Error en la comparación de contraseñas.' });
              }

              if (!isMatch) {
                return res.json({ success: false, message: 'Contraseña incorrecta.' });
              }

              const sessionToken = createSessionToken();
              res.cookie('session_token', sessionToken, { httpOnly: true, secure: false });

              db.query('INSERT INTO sessions (user_id, token) VALUES (?, ?)', [owner.id, sessionToken], (err, results) => {
                if (err) {
                  console.error('Error al guardar el token de sesión en la base de datos:', err);
                  return res.json({ success: false, message: 'Error en la base de datos.' });
                }
                return res.json({ success: true, user_id: owner.id, role: owner.rol, pet_id: pet.usuario_id });
              });
            });
          });
        } else {
          console.log('Usuario o mascota no encontrado.');
          return res.json({ success: false, message: 'Usuario o mascota no encontrado.' });
        }
      });
    }
  });
});

module.exports = router;

