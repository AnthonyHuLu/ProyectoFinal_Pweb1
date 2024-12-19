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
    print "<html><head><title>Error</title></head><body><p>Error: Las contraseñas no coinciden.</p></body></html>";
    exit;
}
if ($email !~ /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) {
    print "<html><head><title>Error</title></head><body><p>Error: Formato de correo electrónico inválido.</p></body></html>";
    exit;
}

my $salt = en_base64(random_bytes(16));
my $password_hash = bcrypt($password, '$2a$10$' . $salt);

my $dbh = DBI->connect("DBI:MariaDB:database=permisos;host=db", "root", "contrasena", {'RaiseError' => 1});

my $sth = $dbh->prepare("SELECT COUNT(*) FROM usuarios WHERE nombre = ? OR correo = ?");
$sth->execute($username, $email);
my ($count) = $sth->fetchrow_array();
if ($count > 0) {
    print "<html><head><title>Error</title></head><body><p>Error: El nombre de usuario o correo ya está en uso.</p></body></html>";
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

# Respuesta de éxito con la nueva estructura de la página
print <<HTML;
<html>
<head>
    <title>Registro Exitoso</title>
    <style>
        .container {
            display: flex;
        }
        .configuracion, .opciones {
            flex: 1;
            padding: 20px;
        }
        .opciones {
            border-left: 1px solid #ccc;
        }
    </style>
</head>
<body>
    <h1>Registro Exitoso</h1>
    <div class="container">
        <div class="configuracion">
            <h2>Configuración de Cuenta</h2>
            <form action="http://localhost:8000/cgi-bin/update_persona.cgi" method="post">
                <input type="hidden" name="user_id" value="<!-- ID del usuario aquí -->">
                <label for="direccion">Dirección:</label><br>
                <input type="text" id="direccion" name="direccion" required><br><br>
                <label for="metodo_pago">Método de Pago:</label><br>
                <input type="text" id="metodo_pago" name="metodo_pago" required><br><br>
                <label for="edad">Edad:</label><br>
                <input type="number" id="edad" name="edad" required><br><br>
                <button type="submit">Guardar Cambios</button>
            </form>
        </div>
        <div class="opciones">
            <h2>Opciones para Mascotas</h2>
            <p>Ya tienes una mascota, regístrala para ser parte de nuestra comunidad y recibir promociones:</p>
            <a href="http://localhost:8080/registro_mascota.html">
                <button>Registrar Mascota</button>
            </a>
            <p>No tienes una mascota, adopta alguna de nuestra comunidad:</p>
            <a href="http://localhost:8080/adopcion.html">
                <button>Adoptar Mascota</button>
            </a>
        </div>
    </div>
</body>
</html>
HTML

