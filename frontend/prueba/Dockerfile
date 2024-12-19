FROM debian:latest

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Actualiza el sistema e instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-fcgid \
    perl \
    libdbi-perl \
    libdbd-mysql-perl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Habilita los módulos de CGI y FastCGI
RUN a2enmod cgi
RUN a2enmod actions

# Copia los archivos CGI y HTML al directorio adecuado
COPY ./cgi-bin/register.cgi /usr/lib/cgi-bin/register.cgi
COPY ./html/form.html /var/www/html/index.html

# Establece los permisos para los archivos CGI
RUN chmod +x /usr/lib/cgi-bin/register.cgi

# Configura el archivo de configuración de Apache
COPY ./apache2.conf /etc/apache2/sites-available/000-default.conf

# Expone el puerto 80
EXPOSE 80

# Inicia el servidor Apache en primer plano usando apache2ctl
CMD ["apache2ctl", "-D", "FOREGROUND"]

