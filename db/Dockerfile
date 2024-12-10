FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=contrasena

EXPOSE 3306

COPY ./db/permisos.sql /docker-entrypoint-initdb.d/
COPY ./db/principal.sql /docker-entrypoint-initdb.d/

RUN mkdir -p /var/lib/mysql-files/images
COPY ./images/ /var/lib/mysql-files/images/

RUN mkdir -p /var/lib/mysql-files/fotos
COPY ./fotos/ /var/lib/mysql-files/fotos/

CMD ["mariadbd"]

