#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use utf8;
use Encode qw(decode encode);
# Configurar la salida como UTF-8
binmode STDOUT, ":encoding(UTF-8)";

# Crear objeto CGI
my $cgi = CGI->new;

# Imprimir encabezado HTTP
print $cgi->header(-type => 'text/html', -charset => 'utf-8');

# Obtener el término de búsqueda
my $query = decode('UTF-8', $cgi->param('q') || '');
$query = uc($query); # Convertir a mayúsculas para una búsqueda sensible a mayúsculas

# Imprimir el inicio del HTML
print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultados de búsqueda</title>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.comcss2family=Hubot+Sans:ital,wght@1,300&family=Playwrite+GB+S:ital,wght@0,100..400;1,100..400&family=Sedgwick+Ave+Display&display=swap" rel="stylesheet">
    <style>
        body {
        font-family: "Hubot Sans", sans-serif;
	font-optical-sizing: auto;
  	font-weight: 300;
  	font-style: italic;
  	font-variation-settings:
    	"wdth" 100;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: calc(100% - 100px);
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px;
            background-color: #5cb85c;
            border: none;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #4cae4c;
        }
        .result {
            border: 1px solid #ddd;
            border-radius: 4px;
            margin: 10px 0;
            padding: 15px;
            background-color: #f9f9f9;
        }
        .result h2 {
            margin: 0;
            font-size: 1.25em;
            color: #252850;
        }
        .result p {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Resultados de búsqueda para: $query</h1>
        <form action="/cgi-bin/busquedaU.cgi" method="get">
            <input type="text" name="q" placeholder="Buscar universidades..." value="$query">
            <button type="submit">Buscar</button>
        </form>
HTML

# Abrir y leer el archivo CSV
open(my $fh, '<:encoding(UTF-8)', '/usr/lib/cgi-bin/universidades_utf8.csv') or die "No se pudo abrir el archivo: $!";

# Leer y descartar la primera línea (encabezados)
my $encabezado = <$fh>;

# Procesar cada línea del CSV
my $resultados = 0;
my @resultados_html;  # Array para almacenar los resultados

while (my $line = <$fh>) {
    chomp $line;
    
    # Decodificar la línea leída para asegurar que se manejen correctamente los caracteres
    my $line_decoded = decode('UTF-8', $line);
    
    # Usar una expresión regular para extraer los 23 campos con el delimitador '|'
    if ($line_decoded =~ /^([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)$/) {
        my ($codigo_entidad, $nombre, $tipo_gestion, $estado_licenciamiento, $periodo_licenciamiento, $codigo_filial, $nombre_filial, $departamento_filial, $provincia_filial, $codigo_local, $departamento_local, $provincia_local, $distrito_local, $latitud_ubicacion, $longitud_ubicacion, $tipo_autorizacion_local, $denominacion_programa, $tipo_nivel_academico, $nivel_academico, $codigo_clase_programa_n2, $nombre_clase_programa_n2, $tipo_autorizacion_programa, $tipo_autorizacion_programa_local) = ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23);
        
        # Convertir a mayúsculas para la comparación
        my $linea_upper = uc("$nombre $tipo_gestion $estado_licenciamiento $denominacion_programa");
        
        # Si la línea contiene el término de búsqueda, almacenar los resultados
        if ($linea_upper =~ /\Q$query\E/) {  # Usar \Q y \E para escapar caracteres especiales
            push @resultados_html, <<RESULT;
            <div class="result">
                <h2>$nombre</h2>
                <p><strong>Código Entidad:</strong> $codigo_entidad</p>
                <p><strong>Estado de licenciamiento:</strong> $estado_licenciamiento</p>
                <p><strong>Denominación del programa:</strong> $denominacion_programa</p>
                <p><strong>Departamento:</strong> $departamento_filial</p>
            </div>
RESULT
            $resultados++;
        }
    }
}

# Cerrar el archivo
close $fh;

# Imprimir el número de resultados al inicio
if ($resultados == 0) {
    print "<p>No se encontraron resultados para \"$query\".</p>";
} else {
    print "<p>Se encontraron $resultados resultados para \"$query\".</p>";
    print join("\n", @resultados_html);  # Imprimir todos los resultados almacenados
}

print <<HTML;
    </div>
</body>
</html>
HTML

