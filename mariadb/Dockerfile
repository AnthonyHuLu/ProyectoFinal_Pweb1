FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=contrasena

EXPOSE 3306

COPY ./sql/permisos.sql /docker-entrypoint-initdb.d/
COPY ./sql/principal.sql /docker-entrypoint-initdb.d/

RUN apt-get update && apt-get install -y \
    mariadb-client

RUN mkdir -p /var/lib/mysql-files/images
COPY ./images/ /var/lib/mysql-files/images/

RUN mkdir -p /var/lib/mysql-files/fotos
COPY ./fotos/ /var/lib/mysql-files/fotos/

HEALTHCHECK --interval=10s --timeout=5s --start-period=1m --retries=5 \
  CMD ["mysqladmin", "ping", "-h", "127.0.0.1", "-u", "root", "-pcontrasena"] || exit 1

CMD ["mariadbd"]

