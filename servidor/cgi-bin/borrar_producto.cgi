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

# Verificar que se recibió un ID válido
if ($id) {
    # Conectar a la base de datos
    my $dbh = DBI->connect("DBI:MariaDB:database=principal;host=db", "root", "contrasena", {'RaiseError' => 1});

    # Borrar el producto de la base de datos
    my $sth = $dbh->prepare("DELETE FROM productos WHERE id=?");
    $sth->execute($id);

    # Desconectar de la base de datos
    $sth->finish();
    $dbh->disconnect();

    # Redireccionar de vuelta al inventario
    print "<html><head><meta http-equiv='refresh' content='0; url=/cgi-bin/ver_inventario.cgi'></head><body></body></html>";
} else {
    # Mostrar un mensaje de error si no se recibe un ID válido
    print "<html><head><title>Error</title></head><body><p>Error: No se proporcionó un ID válido.</p></body></html>";
}

