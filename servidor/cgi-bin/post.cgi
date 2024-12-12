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
    my $nombre = $data->{nombre};
    my $year = $data->{year};
    my $vote = $data->{vote};
    my $score = $data->{score};

    my $sth = $dbh->prepare("INSERT INTO peliculas (nombre, year, vote, score) VALUES (?, ?, ?, ?)");
    $sth->execute($nombre, $year, $vote, $score);
    print encode_json({ resultado => "Película agregada: $nombre" });
} else {
    print encode_json({ error => "Método no soportado" });
}

$dbh->disconnect;
