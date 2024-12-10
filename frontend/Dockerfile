# Dockerfile para el contenedor frontend usando Apache
FROM httpd:latest

# Copiar los archivos de configuración de Apache y el sitio web
COPY . /usr/local/apache2/htdocs/

# Exponer el puerto 80 para el contenedor
EXPOSE 80

CMD ["httpd-foreground"]

