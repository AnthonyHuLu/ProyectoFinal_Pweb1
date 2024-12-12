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

if ($method eq 'GET') {
    my $sth = $dbh->prepare("SELECT * FROM peliculas");
    $sth->execute;

    my @output;
    while (my @row = $sth->fetchrow_array) {
        push @output, {
            pelicula_id => $row[0],
            nombre => $row[1],
            year => $row[2],
            vote => $row[3],
            score => $row[4]
        };
    }
    $sth->finish;
    print encode_json(\@output);
} else {
    print encode_json({ error => "Método no soportado" });
}

$dbh->disconnect;
