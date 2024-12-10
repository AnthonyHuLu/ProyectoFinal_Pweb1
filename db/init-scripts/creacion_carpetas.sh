#!/bin/bash

# Esperar a que MariaDB esté listo
until mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e ";" ; do
    echo "Esperando a que MariaDB esté listo..."
    sleep 5
done

# Crear carpetas para cada mascota en la base de datos
mascotas=$(mysql -u root -p"$MYSQL_ROOT_PASSWORD" -N -e "SELECT nombre FROM permisos.mascotas;")
for mascota in $mascotas; do
    mkdir -p "/var/lib/mysql-files/fotos/$mascota"
    echo "Carpeta creada para $mascota en /var/lib/mysql-files/fotos/$mascota"
done

# Eliminar script después de la ejecución
rm -- "$0"

