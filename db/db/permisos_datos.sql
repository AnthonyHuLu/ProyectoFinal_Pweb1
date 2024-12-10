USE permisos;

INSERT INTO usuarios (nombre, correo, hash_password, rol) VALUES
('Admin', 'admin@empresa.com', 'superadmin', 'admin'),
('Lucas', 'lucas@empresa.com', 'personallucas', 'personal'),
('Tito', 'tito@empresa.com', 'personaltito', 'personal'),
('John', 'john@gmail.com', 'jhonperro', 'duenio'),
('Jane', 'jane@gmail.com', 'janegatoconejo', 'duenio'),
('Roberto', 'roberto@gmail.com', 'robertosinmascota', 'duenio');

INSERT INTO mascotas (nombre, tipo_mascota, dueño_id) VALUES
('Fido', 'Perro', 4),
('Cat', 'Gato', 5),
('Bunny', 'Conejo', 5),
('Matias', 'Perro', 2);

