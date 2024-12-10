-- Crear la base de datos `principal` si no existe
CREATE DATABASE IF NOT EXISTS principal;
-- Utilizar la base de datos `principal`
USE principal;

-- Crear la tabla `publicaciones` para almacenar publicaciones de los dueños
CREATE TABLE publicaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    duenio_id INT,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (duenio_id) REFERENCES permisos.usuarios(id)
);

-- Crear la tabla `perfiles` para almacenar información de perfil de las mascotas
CREATE TABLE perfiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mascota_id INT,
    raza VARCHAR(100),
    caracteristicas TEXT,
    alergias TEXT,
    edad INT,
    FOREIGN KEY (mascota_id) REFERENCES permisos.mascotas(usuario_id)
);

-- Crear la tabla `fotos` para almacenar las fotos subidas por las mascotas
CREATE TABLE fotos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mascota_id INT,
    ruta_foto VARCHAR(255),
    descripcion TEXT,
    fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (mascota_id) REFERENCES permisos.mascotas(usuario_id)
);

-- Crear la tabla `likes_foros` para almacenar los likes en las publicaciones
CREATE TABLE likes_foros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    publicacion_id INT,
    duenio_id INT,
    FOREIGN KEY (publicacion_id) REFERENCES publicaciones(id),
    FOREIGN KEY (duenio_id) REFERENCES permisos.usuarios(id)
);

-- Crear la tabla `productos` para almacenar información sobre los productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    tipo VARCHAR(50),
    precio DECIMAL(10, 2),
    stock INT,
    imagen_ruta VARCHAR(255), -- Campo para almacenar la ruta de la imagen
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear la tabla `tipos_cliente` para almacenar diferentes tipos de clientes
CREATE TABLE tipos_cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL
);

-- Crear la tabla `productos_tipos_cliente` para relacionar productos con tipos de clientes
CREATE TABLE productos_tipos_cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    tipo_cliente_id INT,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (tipo_cliente_id) REFERENCES tipos_cliente(id)
);

-- Crear la tabla `pedidos` para almacenar información sobre los pedidos realizados por las mascotas (clientes)
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mascota_id INT,
    producto_id INT,
    cantidad INT,
    fecha DATE,
    FOREIGN KEY (mascota_id) REFERENCES permisos.mascotas(usuario_id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

