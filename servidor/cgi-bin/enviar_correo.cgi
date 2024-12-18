#!/usr/bin/perl
use strict;
use warnings;
use Email::Sender::Simple qw(sendmail);
use Email::Sender::Transport::SMTP qw();
use Email::Simple;
use Email::Simple::Creator;

# Leer la información del archivo
open(my $fh, '<', '/tmp/correo_info.txt') or die "No se pudo abrir el archivo: $!";
my ($username, $email) = <$fh>;
chomp($username);
chomp($email);
close($fh);

# Enviar correo de bienvenida
sub enviar_correo_bienvenida {
    my ($to, $username) = @_;
    my $email = Email::Simple->create(
        header => [
            To      => $to,
            From    => 'jhuancal@unsa.edu.pe',
            Subject => 'Bienvenido a Nuestra Plataforma',
        ],
        body => "Hola $username,\n\nGracias por registrarte en nuestra plataforma. ¡Esperamos que disfrutes de nuestros servicios!\n\nSaludos,\nEl Equipo WilySavy",
    );

    my $transport = Email::Sender::Transport::SMTP->new({
        host => 'smtp.gmail.com',
        port => 465,                           # Puerto 465 para SSL
        sasl_username => 'jhuancal@unsa.edu.pe',
        sasl_password => 'pghhwptfugmwcscn',
        ssl  => 'ssl',                         # Usar SSL
    });

    sendmail($email, { transport => $transport });
}

eval {
    enviar_correo_bienvenida($email, $username);
};
if ($@) {
    print "Error al enviar el correo de bienvenida: $@";
}

