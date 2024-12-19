const express = require('express');
const router = express.Router();
const mysql = require('mysql');
const bcrypt = require('bcrypt');

const db = mysql.createConnection({
    host: 'db',
    user: 'root',
    password: 'contrasena',
    database: 'permisos'
});

router.post('/', (req, res) => {
    const { nombreMascota, tipoMascota, correoDuenio, contrasenaDuenio } = req.body;

    // Verificar usuario
    db.query('SELECT * FROM usuarios WHERE correo = ?', [correoDuenio], (err, results) => {
        if (err) {
            return res.json({ success: false, message: 'Error en la base de datos.' });
        }

        if (results.length === 0) {
            return res.json({ success: false, message: 'Usuario no encontrado.' });
        }

        const usuario = results[0];
        bcrypt.compare(contrasenaDuenio, usuario.hash_password, (err, isMatch) => {
            if (err) {
                console.error('Error comparando contrase  as:', err);
                return res.json({ success: false, message: 'Error en la comparaci  n de contrase  as.' });
            }

            if (!isMatch) {
                return res.json({ success: false, message: 'Contrase  a incorrecta.' });
            }

            // Insertar mascota
            const duenio_id = usuario.id;
            db.query('INSERT INTO mascotas (nombre, tipo_mascota, duenio_id) VALUES (?, ?, ?)', [nombreMascota, tipoMascota, duenio_id], (err, result) => {
                if (err) {
                    return res.json({ success: false, message: 'Error al registrar la mascota.' });
                }

                return res.json({ success: true, message: 'Mascota registrada exitosamente.' });
            });
        });
    });
});

module.exports = router;

