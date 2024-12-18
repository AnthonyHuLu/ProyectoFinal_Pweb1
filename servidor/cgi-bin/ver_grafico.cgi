#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;
use GD::Graph::pie;

# Crear un objeto CGI
my $cgi = CGI->new;

# Imprimir el encabezado HTTP
print $cgi->header('image/png');

# Conectar a la base de datos
my $dbh = DBI->connect("DBI:MariaDB:database=principal;host=db", "root", "contrasena", {'RaiseError' => 1});

# Preparar y ejecutar la consulta SQL considerando el stock
my $sth = $dbh->prepare("SELECT tipo, SUM(stock) FROM productos GROUP BY tipo");
$sth->execute();

# Obtener los datos para la gráfica
my (@tipos, @cantidades);
while (my @row = $sth->fetchrow_array) {
    push @tipos, $row[0];
    push @cantidades, $row[1];
}

# Crear la gráfica
my $graph = GD::Graph::pie->new(600, 400);  # Ajustar tamaño para mejorar la visibilidad
$graph->set(
    title             => 'Distribución de Productos por Tipo (considerando Stock)',
    label             => 'Productos',
    axislabelclr      => 'black',
    dclrs             => [qw(green blue red yellow purple cyan)],
    transparent       => 0,
    start_angle       => 90,
) or die $graph->error;

my $gd = $graph->plot([\@tipos, \@cantidades]) or die $graph->error;

# Imprimir la gráfica en formato PNG
print $gd->png;

# Desconectar de la base de datos
$sth->finish();
$dbh->disconnect();

