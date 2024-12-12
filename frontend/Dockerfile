FROM httpd:latest

COPY . /usr/local/apache2/htdocs/
RUN mkdir -p /usr/local/apache2/htdocs/images/
COPY ./images/ /usr/local/apache2/htdocs/images/


EXPOSE 80

