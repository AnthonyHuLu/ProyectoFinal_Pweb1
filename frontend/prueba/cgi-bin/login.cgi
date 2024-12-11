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
    my $password = $data->{password};

    # Aquí deberías validar el usuario y la contraseña
    my $sth = $dbh->prepare("SELECT * FROM usuarios WHERE username = ? AND password = ?");
    $sth->execute($username, $password);
    
    if (my $row = $sth->fetchrow_hashref) {
        print encode_json({ resultado => "Inicio de sesión exitoso", usuario => $row->{username} });
    } else {
        print encode_json({ error => "Credenciales incorrectas" });
    }
    $sth->finish;
} else {
    print encode_json({ error => "Método no soportado" });
}

$dbh->disconnect;

