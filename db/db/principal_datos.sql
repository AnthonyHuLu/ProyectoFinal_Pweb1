USE principal;

-- Datos de ejemplo para la tabla `publicaciones`
INSERT INTO publicaciones (duenio_id, titulo, contenido) VALUES
(4, 'Cómo Cuidar a los Perros', 'Aquí tienes algunos consejos para mantener a tu perro feliz y saludable...'),
(5, '¿Pueden Convivir un Gato y un Conejo?', 'Muchas personas se preguntan si es posible que un gato y un conejo vivan juntos. Aquí te damos algunos consejos...'),
(1, 'Mantenimiento de la Plataforma', 'Estamos realizando un mantenimiento programado de la plataforma para mejorar nuestros servicios. Gracias por tu paciencia.'),
(2, 'Guía de Uso para el Personal', 'Aquí hay algunas directrices para el personal sobre cómo utilizar la plataforma de manera efectiva.');

-- Datos de ejemplo para la tabla `perfiles`
INSERT INTO perfiles (mascota_id, raza, caracteristicas, alergias, edad) VALUES
(1, 'Labrador', 'Amigable y enérgico', 'Polen', 3),
(2, 'Siames', 'Juguetón y vocal', 'Polvo', 2);

-- Datos de ejemplo para la tabla `fotos`
INSERT INTO fotos (mascota_id, ruta_foto, descripcion) VALUES
(1, '/fotos/fido/foto1.jpg', 'Foto de Fido'),
(2, '/fotos/cat/foto1.jpg', 'Foto de Cat');

-- Datos de ejemplo para la tabla `likes_foros`
INSERT INTO likes_foros (publicacion_id, duenio_id) VALUES
(1, 4), -- John recibe like por su publicación
(2, 5); -- Jane recibe like por su publicación

-- Datos de ejemplo para la tabla `productos`
INSERT INTO productos (nombre, descripcion, tipo, precio, stock, imagen_ruta) VALUES
('Collar para Perros', 'Collar ajustable para perros de tamaño mediano', 'Perro', 19.99, 50, '/images/collar_perro.jpg'),
('Rascador para Gatos', 'Rascador de sisal para gatos', 'Gato', 29.99, 30, '/images/rascador_gato.jpg'),
('Comedero de Plástico', 'Comedero resistente y duradero', 'General', 9.99, 100, '/images/comedero_plastico.jpg'),
('Peine para Gatos', 'Peine de acero inoxidable para gatos', 'Gato', 12.99, 40, '/images/peine_gato.jpg'),
('Ratoncito a Pilas', 'Juguete para gatos en forma de ratón a pilas', 'Gato', 14.99, 60, '/images/ratoncito_pilas.jpg'),
('Comida para Perros', 'Bolsa de 10 kg de comida para perros', 'Perro', 29.99, 80, '/images/comida_perros.jpg'),
('Jaula para Conejos', 'Jaula espaciosa y segura para conejos', 'Conejo', 59.99, 20, '/images/jaula_conejos.jpg'),
('Comida para Gatos', 'Bolsa de 5 kg de comida para gatos', 'Gato', 24.99, 70, '/images/comida_gatos.jpg');

-- Datos de ejemplo para la tabla `tipos_cliente`
INSERT INTO tipos_cliente (tipo) VALUES
('Perro'),
('Gato'),
('Conejo');

-- Datos de ejemplo para la tabla `productos_tipos_cliente`
INSERT INTO productos_tipos_cliente (producto_id, tipo_cliente_id) VALUES
(1, 1), -- Collar para Perros asociado a tipo cliente Perro
(2, 2), -- Rascador para Gatos asociado a tipo cliente Gato
(3, 1), -- Comedero de Plástico asociado a tipo cliente Perro
(3, 2), -- Comedero de Plástico asociado a tipo cliente Gato
(3, 3), -- Comedero de Plástico asociado a tipo cliente Conejo
(4, 2), -- Peine para Gatos asociado a tipo cliente Gato
(5, 2), -- Ratoncito a Pilas asociado a tipo cliente Gato
(6, 1), -- Comida para Perros asociado a tipo cliente Perro
(7, 3), -- Jaula para Conejos asociado a tipo cliente Conejo
(8, 2); -- Comida para Gatos asociado a tipo cliente Gato

-- Datos de ejemplo para la tabla `pedidos`
INSERT INTO pedidos (mascota_id, producto_id, cantidad, fecha) VALUES
(1, 1, 2, '2023-01-15'), -- Fido compró 2 collares para perros
(2, 2, 1, '2023-01-20'), -- Cat compró 1 rascador para gatos
(1, 3, 1, '2023-01-25'), -- Fido compró 1 comedero de plástico
(2, 5, 3, '2023-02-01'), -- Cat compró 3 ratoncitos a pilas
(2, 8, 1, '2023-02-10'), -- Cat compró 1 bolsa de comida para gatos
(1, 6, 1, '2023-02-15'); -- Fido compró 1 bolsa de comida para perros

