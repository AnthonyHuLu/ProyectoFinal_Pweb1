const mysql = require('mysql');

const db = mysql.createConnection({
  host: 'db',
  user: 'root',
  password: 'contrasena',
  database: 'permisos' // Conectar a la base de datos 'permisos'
});

db.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
  }
  console.log('Connected to the permisos database in auth middleware.');
});

function verifySession(req, res, next) {
  const sessionToken = req.cookies.session_token;
  if (!sessionToken) {
    return res.status(401).json({ success: false, message: 'No session token found.' });
  }

  // Verificar el token de sesión en la base de datos
  db.query('SELECT * FROM sessions WHERE token = ?', [sessionToken], (err, results) => {
    if (err) {
      console.error('Error verifying session token:', err);
      return res.status(500).json({ success: false, message: 'Error verifying session.' });
    }

    if (results.length === 0) {
      return res.status(401).json({ success: false, message: 'Invalid session token.' });
    }

    // Almacena los detalles del usuario en la solicitud para su uso posterior
    req.user = results[0].user_id;
    next();
  });
}

module.exports = verifySession;

