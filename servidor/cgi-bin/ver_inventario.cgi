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
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Inventario de Productos</title>
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
                    <li class="nav-item"><a class="nav-link" href="http://localhost:8080/acerca-de.html.html"><i class="fas fa-phone"></i> Contáctanos</a></li>
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
        <div class="grafico text-center mb-4">
            <img src="/cgi-bin/ver_grafico.cgi" alt="Gráfica de Inventario">
        </div>
        <h1 class="text-center">Inventario de Productos</h1>
        <table class="table table-bordered table-hover">
            <thead class="thead-dark">
                <tr>
                    <th>Nombre</th>
                    <th>Descripción</th>
                    <th>Precio</th>
                    <th>Stock</th>
                    <th>Imagen</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
HTML

while (my @row = $sth->fetchrow_array) {
    my $imagen_ruta = $row[5];
    $imagen_ruta =~ s{^/images/}{};
    my $imagen_url = "/images/$imagen_ruta";

    print <<HTML;
                <tr>
                    <td>
                        <form id="update_form_$row[0]" method="post" action="/cgi-bin/update_producto.cgi">
                            <input type="text" class="form-control" name="nombre_$row[0]" value="$row[1]">
                    </td>
                    <td><textarea class="form-control" name="descripcion_$row[0]">$row[2]</textarea></td>
                    <td><input type="number" class="form-control" name="precio_$row[0]" value="$row[3]" step="0.01"></td>
                    <td><input type="number" class="form-control" name="stock_$row[0]" value="$row[4]"></td>
                    <td><img src="$imagen_url" alt="$row[1]" class="img-fluid" style="max-width: 100px;"></td>
                    <td class="botones">
                        <input type="hidden" name="id" value="$row[0]">
                        <button type="submit" class="btn btn-primary mb-2" form="update_form_$row[0]">Actualizar</button>
                        </form>
                        <form id="delete_form_$row[0]" method="post" action="/cgi-bin/borrar_producto.cgi">
                            <input type="hidden" name="id" value="$row[0]">
                            <button type="submit" class="btn btn-danger" form="delete_form_$row[0]">Borrar</button>
                        </form>
                    </td>
                </tr>
HTML
}

print <<HTML;
            </tbody>
        </table>
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

# Terminar la consulta y desconectar
$sth->finish();
$dbh->disconnect();

