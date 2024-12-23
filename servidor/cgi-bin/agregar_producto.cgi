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
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Producto Agregado</title>
    <link rel="stylesheet" href="http://localhost:8080/css/style_nuevo.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <!-- Copos de nieve -->
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❄️</div>

    <!-- Barra de navegación -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="http://localhost:8080/index.html">Wily Savy</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item"><a class="nav-link" href="http://localhost:8080/foro.html"><i class="fas fa-comments"></i> Foro</a></li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            <i class="fas fa-shopping-cart"></i> Tienda
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="http://localhost:8080/productos.html">Productos</a>
                            <a class="dropdown-item" href="http://localhost:8080/adopcion.html">Adopta</a>
                            <a class="dropdown-item" href="http://localhost:8080/mantenimiento.html">Promos</a>
                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            <i class="fas fa-user"></i> Acceder
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <button class="dropdown-item" id="registerBtn">Registrarse</button>
                            <button class="dropdown-item" id="loginBtn">Iniciar Sesión</button>
                        </div>
                    </li>
                    <li class="nav-item"><a class="nav-link" href="http://localhost:8080/mantenimiento.html"><i class="fas fa-shopping-cart"></i> Eventos</a></li>
                    <li class="nav-item"><a class="nav-link" href="http://localhost:8080/acerca-de.html"><i class="fas fa-phone"></i> Contáctanos</a></li>
                    <li class="nav-item">
                        <form class="form-inline my-2 my-lg-0">
                            <input class="form-control mr-sm-2" type="search" placeholder="Buscar..." aria-label="Search">
                            <button class="btn btn-outline-light my-2 my-sm-0" type="submit"><i class="fas fa-search"></i></button>
                        </form>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Contenido Principal -->
    <div class="container mt-5">
        <h1 class="text-center">Producto Agregado</h1>
        <p class="lead text-center">El producto <strong>$nombre</strong> ha sido agregado con éxito.</p>
        <div class="vista-previa row">
            <div class="col-md-4">
                <img src="/images/$filename" class="img-fluid rounded" alt="$nombre">
            </div>
            <div class="detalles col-md-8">
                <p><strong>Descripción:</strong> $descripcion</p>
                <p><strong>Precio:</strong> \$$precio</p>
                <p><strong>Stock:</strong> $stock</p>
                <p><strong>Tipo:</strong> $tipo</p>
            </div>
        </div>
        <div class="botones text-center mt-4">
            <button class="btn btn-primary" onclick="window.location.href='http://localhost:8080/agregar_producto.html'">Agregar Otro Producto</button>
            <button class="btn btn-secondary" onclick="window.location.href='http://localhost:8000/cgi-bin/ver_inventario.cgi'">Ver Inventario</button>
            <button class="btn btn-success" onclick="window.location.href='http://localhost:8080/pedidos.html'">Revisar Pedidos</button>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3 mt-4">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <p>&copy; 2024 WilySavy Group, Inc.</p>
                </div>
                <div class="col-md-4">
                    <ul class="list-unstyled">
                        <li><a href="http://localhost:8080/acerca-de.html" class="text-white">¿Quiénes somos?</a></li>
                        <li><a href="#" class="text-white">Políticas de Cookies</a></li>
                        <li><a href="#" class="text-white">Ubicaciones y Sedes</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <ul class="list-unstyled social-media">
                        <li><a href="#" class="text-white"><i class="fab fa-facebook"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
HTML

