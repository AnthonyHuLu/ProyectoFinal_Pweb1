CREATE DATABASE IF NOT EXISTS principal;

USE principal;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    imagen_ruta VARCHAR(255) NOT NULL
);

-- Insertar datos iniciales si es necesario
INSERT INTO productos (nombre, precio, imagen_ruta) VALUES
('Producto1', 10.00, 'ruta/imagens1.jpg'),
('Producto2', 15.00, 'ruta/imagens2.jpg');

