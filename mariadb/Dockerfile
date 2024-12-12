FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=contrasena

EXPOSE 3306

COPY ./sql/permisos.sql /docker-entrypoint-initdb.d/
COPY ./sql/principal.sql /docker-entrypoint-initdb.d/

RUN mkdir -p /var/lib/mysql-files/images
COPY ./images/ /var/lib/mysql-files/images/

RUN mkdir -p /var/lib/mysql-files/fotos
COPY ./fotos/ /var/lib/mysql-files/fotos/

CMD ["mariadbd"]

