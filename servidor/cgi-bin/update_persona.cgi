#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

my $cgi = CGI->new;

# Imprimir el encabezado HTTP
print $cgi->header('text/html; charset=UTF-8');

# Obtener los parámetros del formulario
my $user_id = $cgi->param('user_id') || '';
my $direccion = $cgi->param('direccion') || '';
my $metodo_pago = $cgi->param('metodo_pago') || '';
my $edad = $cgi->param('edad') || '';

# Conectar a la base de datos
my $dbh = DBI->connect("DBI:MariaDB:database=permisos;host=db", "root", "contrasena", {'RaiseError' => 1});

# Actualizar la información del usuario
my $sth = $dbh->prepare("UPDATE usuarios SET direccion = ?, metodo_pago = ?, edad = ? WHERE id = ?");
$sth->execute($direccion, $metodo_pago, $edad, $user_id);

# Desconectar de la base de datos
$sth->finish();
$dbh->disconnect();

# Respuesta de éxito
print <<HTML;
<html>
<head>
    <title>Actualización Exitosa</title>
    <meta http-equiv="refresh" content="3;url=/configuracion_cuenta.html">
</head>
<body>
    <h1>Actualización Exitosa</h1>
    <p>La información de tu cuenta ha sido actualizada con éxito.</p>
</body>
</html>
HTML

