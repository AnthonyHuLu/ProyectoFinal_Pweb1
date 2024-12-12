CREATE DATABASE IF NOT EXISTS permisos;

USE permisos;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    hash_password VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'personal', 'duenio') NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE mascotas (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo_mascota VARCHAR(50) NOT NULL,
    duenio_id INT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (duenio_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (nombre, correo, hash_password, rol) VALUES
('Admin', 'admin@empresa.com', 'superadmin', 'admin'),
('Lucas', 'lucas@empresa.com', 'personallucas', 'personal'),
('Tito', 'tito@empresa.com', 'personaltito', 'personal'),
('John', 'john@gmail.com', 'jhonperro', 'duenio'),
('Jane', 'jane@gmail.com', 'janegatoconejo', 'duenio'),
('Roberto', 'roberto@gmail.com', 'robertosinmascota', 'duenio');

INSERT INTO mascotas (nombre, tipo_mascota, duenio_id) VALUES
('Fido', 'Perro', 4),
('Cat', 'Gato', 5),
('Bunny', 'Conejo', 5),
('Matias', 'Perro', 2);

