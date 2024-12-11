#!/usr/bin/perl
use strict;
use warnings;
use CGI qw/:standard/;
use DBI;
use utf8;
use JSON;

my $database = "prueba";
my $hostname = "mariadb-container";
my $port     = 3306;
my $user     = "root";
my $password = "tu_contrasena_segura";

my $dsn = "DBI:mysql:database=$database;host=$hostname;port=$port";
my $dbh = DBI->connect($dsn, $user, $password, { RaiseError => 1, PrintError => 0 });

my $cgi = CGI->new;
print $cgi->header(-type => 'application/json', -charset => 'UTF-8');

my $method = $cgi->request_method;
my $input = $cgi->param('POSTDATA');
my $data = decode_json($input) if $input;

if ($method eq 'POST') {
    my $username = $data->{username};
    my $email = $data->{email};
    my $password = $data->{password};
    my $role = $data->{role};

    # Verificar si el usuario ya existe
    my $sth = $dbh->prepare("SELECT * FROM usuarios WHERE username = ? OR email = ?");
    $sth->execute($username, $email);
    
    if ($sth->fetchrow_array) {
        print encode_json({ error => "El usuario o el correo ya están en uso." });
    } else {
        # Insertar nuevo usuario
        $sth = $dbh->prepare("INSERT INTO usuarios (username, email, password, role) VALUES (?, ?, ?, ?)");
        $sth->execute($username, $email, $password, $role);
        print encode_json({ resultado => "Usuario registrado exitosamente." });
    }
    $sth->finish;
} else {
    print encode_json({ error => "Método no soportado" });
}

$dbh->disconnect;

