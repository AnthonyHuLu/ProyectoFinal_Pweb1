
FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=contrasena

EXPOSE 3306

# Copiar los scripts de inicialización
COPY ./db/permisos_esquema.sql /docker-entrypoint-initdb.d/
COPY ./db/principal_esquema.sql /docker-entrypoint-initdb.d/
COPY ./db/permisos_datos.sql /docker-entrypoint-initdb.d/
COPY ./db/principal_datos.sql /docker-entrypoint-initdb.d/
COPY ./init-scripts/creacion_carpetas.sh /docker-entrypoint-initdb.d/

# Crear y copiar la carpeta para las imágenes de productos
RUN mkdir -p /var/lib/mysql-files/images
COPY ./images/ /var/lib/mysql-files/images/

# Crear carpeta para las fotos de mascotas
RUN mkdir -p /var/lib/mysql-files/fotos

# Copiar fotos de mascotas
COPY ./fotos/ /var/lib/mysql-files/fotos/

CMD ["mariadbd"]

