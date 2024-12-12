#!/usr/bin/perl
use strict;
use warnings;
use CGI qw/:standard/;
use DBI;
use JSON;
use Crypt::Eksblowfish::Bcrypt qw(bcrypt_hash_en_base64);
use Encode qw(encode decode);
use Try::Tiny;

# Configuración de la base de datos
my $database = "prueba";
my $hostname = "mariadb-container";
my $port     = 3306;
my $user     = "root";
my $password = "tu_contrasena_segura";

my $dsn = "DBI:mysql:database=$database;host=$hostname;port=$port;charset=utf8";  # Agregar charset
my $dbh;

try {
    $dbh = DBI->connect($dsn, $user, $password, { RaiseError => 1, PrintError => 0, mysql_enable_utf8 => 1 });
} catch {
    print encode_json({ error => "No se pudo conectar a la base de datos: $_" });
    exit;
};

my $cgi = CGI->new;
print $cgi->header(-type => 'application/json', -charset => 'UTF-8');

my $method = $cgi->request_method;
my $input = $cgi->param('POSTDATA');
my $data = decode_json($input) if $input;

if ($method eq 'POST') {
    my $username = decode('UTF-8', $data->{username});
    my $email = decode('UTF-8', $data->{email});
    my $password = $data->{password};  # Se puede dejar sin decodificar, ya que se usa para hashing
    my $role = decode('UTF-8', $data->{role});

    # Verificar si el usuario ya existe
    my $sth = $dbh->prepare("SELECT * FROM usuarios WHERE username = ? OR email = ?");
    $sth->execute($username, $email);
    
    if ($sth->fetchrow_array) {
        print encode_json({ error => "El usuario o el correo ya están en uso." });
    } else {
        # Hash de la contraseña
        my $hashed_password = bcrypt_hash_en_base64($password);

        # Insertar nuevo usuario
        $sth = $dbh->prepare("INSERT INTO usuarios (username, email, password, role) VALUES (?, ?, ?, ?)");
        $sth->execute($username, $email, $hashed_password, $role);
        print encode_json({ resultado => "Usuario registrado exitosamente." });
    }
    $sth->finish;
} else {
    print encode_json({ error => "Método no soportado" });
}

$dbh->disconnect if $dbh;

