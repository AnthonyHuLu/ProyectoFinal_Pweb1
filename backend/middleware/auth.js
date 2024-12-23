const mysql = require('mysql');

const db = mysql.createConnection({
  host: 'db',
  user: 'root',
  password: 'contrasena',
  database: 'permisos'
});

db.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
  }
  console.log('Connected to the permisos database in auth middleware.');
});

function verifySession(req, res, next) {
  const sessionToken = req.cookies.session_token;
  console.log('Verifying session token:', sessionToken); // Mostrar el token de sesi  n recibido

  if (!sessionToken) {
    return res.status(401).json({ success: false, message: 'No session token found.' });
  }

  db.query('SELECT * FROM sessions WHERE token = ?', [sessionToken], (err, results) => {
    if (err) {
      console.error('Error verifying session token:', err);
      return res.status(500).json({ success: false, message: 'Error verifying session.' });
    }

    if (results.length === 0) {
      console.log('Invalid session token:', sessionToken); // Mostrar tokens no v  lidos
      return res.status(401).json({ success: false, message: 'Invalid session token.' });
    }

    req.user = results[0].user_id;
    next();
  });
}
module.exports = verifySession;

