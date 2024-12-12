CREATE DATABASE IF NOT EXISTS principal;

USE principal;

CREATE TABLE publicaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    duenio_id INT,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (duenio_id) REFERENCES permisos.usuarios(id)
);

CREATE TABLE perfiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mascota_id INT,
    raza VARCHAR(100),
    caracteristicas TEXT,
    alergias TEXT,
    edad INT,
    FOREIGN KEY (mascota_id) REFERENCES permisos.mascotas(usuario_id)
);

CREATE TABLE fotos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mascota_id INT,
    ruta_foto VARCHAR(255),
    descripcion TEXT,
    fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (mascota_id) REFERENCES permisos.mascotas(usuario_id)
);

CREATE TABLE likes_foros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    publicacion_id INT,
    duenio_id INT,
    FOREIGN KEY (publicacion_id) REFERENCES publicaciones(id),
    FOREIGN KEY (duenio_id) REFERENCES permisos.usuarios(id)
);

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    tipo VARCHAR(50),
    precio DECIMAL(10, 2),
    stock INT,
    imagen_ruta VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tipos_cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL
);

CREATE TABLE productos_tipos_cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    tipo_cliente_id INT,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (tipo_cliente_id) REFERENCES tipos_cliente(id)
);

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mascota_id INT,
    producto_id INT,
    cantidad INT,
    fecha DATE,
    FOREIGN KEY (mascota_id) REFERENCES permisos.mascotas(usuario_id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

INSERT INTO publicaciones (duenio_id, titulo, contenido) VALUES
(4, 'Cómo Cuidar a los Perros', 'Aquí tienes algunos consejos para mantener a tu perro feliz y saludable...'),
(5, '¿Pueden Convivir un Gato y un Conejo?', 'Muchas personas se preguntan si es posible que un gato y un conejo vivan juntos. Aquí te damos algunos consejos...'),
(1, 'Mantenimiento de la Plataforma', 'Estamos realizando un mantenimiento programado de la plataforma para mejorar nuestros servicios. Gracias por tu paciencia.'),
(2, 'Guía de Uso para el Personal', 'Aquí hay algunas directrices para el personal sobre cómo utilizar la plataforma de manera efectiva.');

INSERT INTO perfiles (mascota_id, raza, caracteristicas, alergias, edad) VALUES
(1, 'Labrador', 'Amigable y enérgico', 'Polen', 3),
(2, 'Siames', 'Juguetón y vocal', 'Polvo', 2);

INSERT INTO fotos (mascota_id, ruta_foto, descripcion) VALUES
(1, '/fotos/fido/foto1.jpg', 'Foto de Fido'),
(2, '/fotos/cat/foto1.jpg', 'Foto de Cat');

INSERT INTO likes_foros (publicacion_id, duenio_id) VALUES
(1, 4),
(2, 5);

INSERT INTO productos (nombre, descripcion, tipo, precio, stock, imagen_ruta) VALUES
('Collar para Perros', 'Collar ajustable para perros de tamaño mediano', 'Perro', 19.99, 50, '/images/collar_perro.jpg'),
('Rascador para Gatos', 'Rascador de sisal para gatos', 'Gato', 29.99, 30, '/images/rascador_gato.jpg'),
('Comedero de Plástico', 'Comedero resistente y duradero', 'General', 9.99, 100, '/images/comedero_plastico.jpg'),
('Peine para Gatos', 'Peine de acero inoxidable para gatos', 'Gato', 12.99, 40, '/images/peine_gato.jpg'),
('Ratoncito a Pilas', 'Juguete para gatos en forma de ratón a pilas', 'Gato', 14.99, 60, '/images/ratoncito_pilas.jpg'),
('Comida para Perros', 'Bolsa de 10 kg de comida para perros', 'Perro', 29.99, 80, '/images/comida_perros.jpg'),
('Jaula para Conejos', 'Jaula espaciosa y segura para conejos', 'Conejo', 59.99, 20, '/images/jaula_conejos.jpg'),
('Comida para Gatos', 'Bolsa de 5 kg de comida para gatos', 'Gato', 24.99, 70, '/images/comida_gatos.jpg');

INSERT INTO tipos_cliente (tipo) VALUES 
('Perro'), ('Gato'), ('Conejo'); 

INSERT INTO productos_tipos_cliente (producto_id, tipo_cliente_id) VALUES 
(1, 1), (2, 2), (3, 1), (3, 2), (3, 3), (4, 2), (5, 2), (6, 1), (7, 3), (8, 2); 

INSERT INTO pedidos (mascota_id, producto_id, cantidad, fecha) VALUES 
(1, 1, 2, '2023-01-15'),
(2, 2, 1, '2023-01-20'),
(1, 3, 1, '2023-01-25'),
(2, 5, 3, '2023-02-01'),
(2, 8, 1, '2023-02-10'),
(1, 6, 1, '2023-02-15');

