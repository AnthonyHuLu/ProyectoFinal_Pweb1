-- Verificar si el usuario 'root' existe antes de crearlo
CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'contrasena';

-- Otorgar todos los privilegios al usuario 'root'
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
FLUSH PRIVILEGES;

