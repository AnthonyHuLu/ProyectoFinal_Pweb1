#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

# Crear un objeto CGI
my $cgi = CGI->new;

# Imprimir el encabezado HTTP
print $cgi->header('text/html; charset=UTF-8');

# Conectar a la base de datos
my $dbh = DBI->connect("DBI:MariaDB:database=principal;host=db", "root", "contrasena", {'RaiseError' => 1});

# Preparar la consulta SQL
my $sth = $dbh->prepare("SELECT id, nombre, descripcion, precio, stock, imagen_ruta FROM productos");
$sth->execute();

# Generar la página HTML
print <<HTML;
<html>
<head>
    <title>Inventario de Productos</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { display: flex; flex-direction: column; align-items: center; }
        .grafico { margin-bottom: 20px; }
        table { border-collapse: collapse; width: 80%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
        th, td { text-align: center; }
        .botones { display: flex; flex-direction: column; align-items: center; }
        .botones button { margin: 5px 0; }
    </style>
</head>
<body>
<div class="container">
    <div class="grafico">
        <img src="/cgi-bin/ver_grafico.cgi" alt="Gráfica de Inventario">
    </div>
    <div>
        <h1>Inventario de Productos</h1>
        <table>
            <tr><th>Nombre</th><th>Descripción</th><th>Precio</th><th>Stock</th><th>Imagen</th><th>Acciones</th></tr>
HTML

while (my @row = $sth->fetchrow_array) {
    my $imagen_ruta = $row[5];
    $imagen_ruta =~ s{^/images/}{};
    my $imagen_url = "/images/$imagen_ruta";

    print <<HTML;
            <tr>
                <td><form id="update_form_$row[0]" method="post" action="/cgi-bin/update_producto.cgi">
                    <input type="text" name="nombre_$row[0]" value="$row[1]">
                </td>
                <td><textarea name="descripcion_$row[0]">$row[2]</textarea></td>
                <td><input type="number" name="precio_$row[0]" value="$row[3]" step="0.01"></td>
                <td><input type="number" name="stock_$row[0]" value="$row[4]"></td>
                <td><img src="$imagen_url" alt="$row[1]" width="100"></td>
                <td class="botones">
                    <input type="hidden" name="id" value="$row[0]">
                    <button type="submit" form="update_form_$row[0]">Actualizar</button>
                </form>
                    <form id="delete_form_$row[0]" method="post" action="/cgi-bin/borrar_producto.cgi">
                        <input type="hidden" name="id" value="$row[0]">
                        <button type="submit" form="delete_form_$row[0]">Borrar</button>
                    </form>
                </td>
            </tr>
HTML
}

print <<HTML;
        </table>
    </div>
</div>
</body>
</html>
HTML

# Terminar la consulta y desconectar
$sth->finish();
$dbh->disconnect();

