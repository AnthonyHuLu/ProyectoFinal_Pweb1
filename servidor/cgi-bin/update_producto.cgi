#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

# Crear un objeto CGI
my $cgi = CGI->new;

# Imprimir el encabezado HTTP
print $cgi->header('text/html; charset=UTF-8');

# Obtener los parámetros del formulario
my $id = $cgi->param('id') || '';
my $nombre = $cgi->param("nombre_$id") || '';
my $descripcion = $cgi->param("descripcion_$id") || '';
my $precio = $cgi->param("precio_$id") || '';
my $stock = $cgi->param("stock_$id") || '';

# Conectar a la base de datos
my $dbh = DBI->connect("DBI:MariaDB:database=principal;host=db", "root", "contrasena", {'RaiseError' => 1});

# Actualizar el producto en la base de datos
my $sth = $dbh->prepare("UPDATE productos SET nombre=?, descripcion=?, precio=?, stock=? WHERE id=?");
$sth->execute($nombre, $descripcion, $precio, $stock, $id);

# Desconectar de la base de datos
$sth->finish();
$dbh->disconnect();

# Redireccionar de vuelta al inventario
print "<html><head><meta http-equiv='refresh' content='0; url=/cgi-bin/ver_inventario.cgi'></head><body></body></html>";

