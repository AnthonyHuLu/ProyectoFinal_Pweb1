#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;
use File::Basename;

my $cgi = CGI->new;

print $cgi->header('text/html; charset=UTF-8');

my $nombre = $cgi->param('nombre') || '';
my $descripcion = $cgi->param('descripcion') || '';
my $precio = $cgi->param('precio') || '';
my $stock = $cgi->param('stock') || '';
my $tipo = $cgi->param('tipo') || '';
my $upload_dir = "/usr/src/app/images";

my $upload_filehandle = $cgi->upload('imagen');
my $filename = basename($cgi->param('imagen'));
my $upload_path = "$upload_dir/$filename";

if ($upload_filehandle) {
    open(my $upload_fh, '>', $upload_path) or die "No se pudo abrir $upload_path para escribir: $!";
    binmode $upload_fh;
    while (my $chunk = <$upload_filehandle>) {
        print $upload_fh $chunk;
    }
    close $upload_fh;
}

my $dbh = DBI->connect("DBI:MariaDB:database=principal;host=db", "root", "contrasena", {'RaiseError' => 1});

my $sth = $dbh->prepare("INSERT INTO productos (nombre, descripcion, precio, stock, tipo, imagen_ruta) VALUES (?, ?, ?, ?, ?, ?)");
$sth->execute($nombre, $descripcion, $precio, $stock, $tipo, $filename);

$sth->finish();
$dbh->disconnect();

print <<HTML;
<html>
<head>
    <title>Producto Agregado</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        .vista-previa {
            display: flex;
            margin-top: 20px;
        }
        .vista-previa img {
            max-width: 150px;
            margin-right: 20px;
        }
        .vista-previa .detalles {
            flex: 1;
        }
        .detalles p {
            margin: 5px 0;
        }
        .botones {
            margin-top: 20px;
        }
        .botones button {
            margin: 5px;
            padding: 10px 15px;
            border: none;
            background-color: #5cb85c;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }
        .botones button:hover {
            background-color: #4cae4c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Producto Agregado</h1>
        <p>El producto <strong>$nombre</strong> ha sido agregado con éxito.</p>
        <div class="vista-previa">
            <img src="/images/$filename" alt="$nombre">
            <div class="detalles">
                <p><strong>Descripción:</strong> $descripcion</p>
                <p><strong>Precio:</strong> \$$precio</p>
                <p><strong>Stock:</strong> $stock</p>
                <p><strong>Tipo:</strong> $tipo</p>
            </div>
        </div>
        <div class="botones">
            <button onclick="window.location.href='http://localhost:8080/agregar_producto.html'">Agregar Otro Producto</button>
            <button onclick="window.location.href='http://localhost:8000/cgi-bin/ver_inventario.cgi'">Ver Inventario</button>
            <button onclick="window.location.href='http://localhost:8080/revisar_pedidos.html'">Revisar Pedidos</button>
        </div>
    </div>
</body>
</html>
HTML

