const express = require('express');
const router = express.Router();

router.post('/', (req, res) => {
  res.clearCookie('session_token');
  return res.json({ success: true, message: 'Logged out successfully.' });
});

module.exports = router;

