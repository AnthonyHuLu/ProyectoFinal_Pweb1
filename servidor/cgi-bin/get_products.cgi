#!/usr/bin/perl
use strict;
use warnings;
use DBI;
use JSON;

# Configuración de la base de datos
my $host = 'db';  # Nombre del contenedor de la base de datos en Docker
my $database = 'nombre_basedatos';
my $user = 'root';
my $password = 'contrasena';

# Conexión a la base de datos
my $dbh = DBI->connect("DBI:mysql:database=$database;host=$host", $user, $password, { RaiseError => 1, AutoCommit => 1 });

# Consulta para obtener los productos
my $query = 'SELECT nombre, precio, CONCAT("/images/", imagen) AS imagen_ruta FROM productos';
my $sth = $dbh->prepare($query);
$sth->execute();

# Generar el JSON
my @productos;
while (my $row = $sth->fetchrow_hashref()) {
    push @productos, $row;
}
$sth->finish();
$dbh->disconnect();

# Enviar el encabezado y la respuesta JSON
print "Content-type: application/json\n\n";
print encode_json(\@productos);