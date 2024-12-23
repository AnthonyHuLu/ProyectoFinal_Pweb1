#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;
use Crypt::Eksblowfish::Bcrypt qw(bcrypt en_base64);
use Bytes::Random::Secure qw(random_bytes);

my $cgi = CGI->new;

print $cgi->header('text/html; charset=UTF-8');

my $username = $cgi->param('username') || '';
my $email = $cgi->param('email') || '';
my $password = $cgi->param('password') || '';
my $confirm_password = $cgi->param('confirm_password') || '';
my $role = $cgi->param('role') || '';

if ($password ne $confirm_password) {
    print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
    <link rel="stylesheet" href="http://localhost:8080/css/style_nuevo.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Error</h1>
        <p class="lead">Las contraseñas no coinciden.</p>
        <button class="btn btn-primary" onclick="window.history.back()">Volver</button>
    </div>
</body>
</html>
HTML
    exit;
}

if ($email !~ /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) {
    print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
    <link rel="stylesheet" href="http://localhost:8080/css/style_nuevo.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Error</h1>
        <p class="lead">Formato de correo electrónico inválido.</p>
        <button class="btn btn-primary" onclick="window.history.back()">Volver</button>
    </div>
</body>
</html>
HTML
    exit;
}

my $salt = en_base64(random_bytes(16));
my $password_hash = bcrypt($password, '$2a$10$' . $salt);

my $dbh = DBI->connect("DBI:MariaDB:database=permisos;host=db", "root", "contrasena", {'RaiseError' => 1});

my $sth = $dbh->prepare("SELECT COUNT(*) FROM usuarios WHERE nombre = ? OR correo = ?");
$sth->execute($username, $email);
my ($count) = $sth->fetchrow_array();
if ($count > 0) {
    print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
    <link rel="stylesheet" href="http://localhost:8080/css/style_nuevo.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Error</h1>
        <p class="lead">El nombre de usuario o correo ya está en uso.</p>
        <button class="btn btn-primary" onclick="window.history.back()">Volver</button>
    </div>
</body>
</html>
HTML
    exit;
}

# Insertar el nuevo usuario en la base de datos
$sth = $dbh->prepare("INSERT INTO usuarios (nombre, correo, hash_password, rol) VALUES (?, ?, ?, ?)");
$sth->execute($username, $email, $password_hash, $role);

# Generar el archivo para enviar el correo
open(my $fh, '>', '/tmp/correo_info.txt') or die "No se pudo abrir el archivo: $!";
print $fh "$username\n$email\n";
close($fh);

# Ejecutar el script de envío de correo
system("/usr/lib/cgi-bin/enviar_correo.cgi");

# Desconectar de la base de datos
$sth->finish();
$dbh->disconnect();

print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro Exitoso</title>
    <link rel="stylesheet" href="http://localhost:8080/css/style_nuevo.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Registro Exitoso</h1>
        <div class="configuracion mt-4">
            <h2>Configuración de Cuenta</h2>
            <form action="http://localhost:8000/cgi-bin/update_persona.cgi" method="post">
                <input type="hidden" name="user_id" value="<!-- ID del usuario aquí -->">
                <div class="form-group">
                    <label for="direccion">Dirección:</label>
                    <input type="text" class="form-control" id="direccion" name="direccion" required>
                </div>
                <div class="form-group">
                    <label for="metodo_pago">Método de Pago:</label>
                    <input type="text" class="form-control" id="metodo_pago" name="metodo_pago" required>
                </div>
                <div class="form-group">
                    <label for="edad">Edad:</label>
                    <input type="number" class="form-control" id="edad" name="edad" required>
                </div>
                <button type="submit" class="btn btn-success">Guardar Cambios</button>
            </form>
        </div>
        <div class="opciones mt-4">
            <h2>Opciones para Mascotas</h2>
            <p>Ya tienes una mascota, regístrala para ser parte de nuestra comunidad y recibir promociones:</p>
            <a href="http://localhost:8080/registro_mascota.html" class="btn btn-primary">Registrar Mascota</a>
            <p class="mt-3">No tienes una mascota, adopta alguna de nuestra comunidad:</p>
            <a href="http://localhost:8080/adopcion.html" class="btn btn-secondary">Adoptar Mascota</a>
        </div>
    </div>
</body>
</html>
HTML

