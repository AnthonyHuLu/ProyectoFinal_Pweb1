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

