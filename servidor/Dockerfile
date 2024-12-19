# Usar una imagen base de Debian
FROM debian:latest

# Instalar Apache, Perl y módulos necesarios
RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-perl2 perl cpanminus locales && \
    apt-get install -y libwww-perl && \
    apt-get install -y nano && \
    apt-get install -y build-essential default-libmysqlclient-dev libmariadb-dev libssl-dev pkg-config libgd-dev && \
    apt-get install -y libemail-sender-perl libemail-simple-perl libemail-mime-perl && \
    cpanm CGI && \
    cpanm DBI && \
    cpanm DBD::MariaDB && \
    cpanm GD::Graph && \
    cpanm Email::Sender && \
    cpanm GD && \
    cpanm GD::Graph && \
    cpan Digest::SHA && \
    apt-get clean

# Generar locales y establecer la configuración de UTF-8
RUN echo "es_ES.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=es_ES.UTF-8

# Configurar variables de entorno para UTF-8
ENV LANG=es_ES.UTF-8
ENV LANGUAGE=es_ES:es
ENV LC_ALL=es_ES.UTF-8

# Habilitar los módulos necesarios de Apache
RUN a2enmod cgi
RUN a2enmod rewrite
RUN a2enmod ssl

# Crear directorios necesarios
RUN mkdir -p /usr/lib/cgi-bin/ /usr/src/app/images/

# Copiar archivos al contenedor
COPY ./cgi-bin/ /usr/lib/cgi-bin/
COPY ./images/ /usr/src/app/images/
COPY ./apache2.conf /etc/apache2/apache2.conf
COPY ./000-default.conf /etc/apache2/sites-available/000-default.conf

# Configurar permisos para los scripts y directorios CGI
RUN chmod +x /usr/lib/cgi-bin/*.cgi
RUN chmod 644 /usr/src/app/images/*
RUN chown www-data:www-data /usr/src/app/images/*

# Configurar Apache para manejar UTF-8
RUN echo 'AddDefaultCharset UTF-8' >> /etc/apache2/apache2.conf

RUN a2dismod mpm_prefork mpm_worker && a2enmod mpm_event

# Exponer el puerto 80
EXPOSE 80

# Instalar librerías adicionales después de los pasos anteriores
RUN cpanm Crypt::Eksblowfish && \
    cpanm Bytes::Random::Secure

# Iniciar Apache en primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]
