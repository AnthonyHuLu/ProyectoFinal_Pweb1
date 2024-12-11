#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

# Crear objeto CGI
my $cgi = CGI->new;

# Generar encabezado HTTP
print $cgi->header('text/html');

# Configuración de la base de datos
my $dsn = "DBI:mysql:database=petstore;host=mariadb;port=3306";
my $db_user = "root";
my $db_password = "mypassword";

# Conectar a la base de datos
my $dbh = DBI->connect($dsn, $db_user, $db_password, {
    RaiseError => 1,
    AutoCommit => 1,
});

if (!$dbh) {
    print "<h1>Error: No se pudo conectar a la base de datos</h1>";
    exit;
}

# Generar interfaz de usuario
print "<html><head><title>Inventario</title></head><body>";
print "<h1>Gestión de Inventario</h1>";
print "<form method='post' action='script.cgi'>";
print "<label for='accion'>Seleccione una acción:</label>";
print "<select name='accion' id='accion'>";
print "  <option value='listar'>Listar Productos</option>";
print "  <option value='agregar'>Agregar Producto</option>";
print "  <option value='actualizar'>Actualizar Stock</option>";
print "  <option value='eliminar'>Eliminar Producto</option>";
print "</select><br><br>";
print "<input type='submit' value='Ejecutar'>";
print "</form>";

# Obtener acción seleccionada
my $accion = $cgi->param('accion') || '';

if ($accion eq 'listar') {
    # Listar productos
    my $sth = $dbh->prepare("SELECT * FROM productos");
    $sth->execute();

    print "<h2>Lista de Productos</h2><table border='1'>";
    print "<tr><th>ID</th><th>Nombre</th><th>Descripción</th><th>Tipo</th><th>Precio</th><th>Stock</th><th>Imagen</th></tr>";

    while (my $row = $sth->fetchrow_hashref) {
        print "<tr>";
        print "<td>$row->{id}</td>";
        print "<td>$row->{nombre}</td>";
        print "<td>$row->{descripcion}</td>";
        print "<td>$row->{tipo}</td>";
        print "<td>\$ $row->{precio}</td>";
        print "<td>$row->{stock}</td>";
        print "<td><img src='$row->{imagen_ruta}' alt='$row->{nombre}' width='50'></td>";
        print "</tr>";
    }

    print "</table>";
    $sth->finish;

} elsif ($accion eq 'agregar') {
    # Formulario para agregar producto
    print "<h2>Agregar Producto</h2>";
    print "<form method='post' action='script.cgi'>";
    print "<input type='hidden' name='accion' value='insertar'>";
    print "Nombre: <input type='text' name='nombre' required><br>";
    print "Descripción: <input type='text' name='descripcion' required><br>";
    print "Tipo: <input type='text' name='tipo' required><br>";
    print "Precio: <input type='number' step='0.01' name='precio' required><br>";
    print "Stock: <input type='number' name='stock' required><br>";
    print "Ruta de Imagen: <input type='text' name='imagen_ruta' required><br>";
    print "<input type='submit' value='Agregar Producto'>";
    print "</form>";

} elsif ($accion eq 'insertar') {
    # Insertar producto en la base de datos
    my $nombre = $cgi->param('nombre');
    my $descripcion = $cgi->param('descripcion');
    my $tipo = $cgi->param('tipo');
    my $precio = $cgi->param('precio');
    my $stock = $cgi->param('stock');
    my $imagen_ruta = $cgi->param('imagen_ruta');

    my $sth = $dbh->prepare("INSERT INTO productos (nombre, descripcion, tipo, precio, stock, imagen_ruta) VALUES (?, ?, ?, ?, ?, ?)");
    $sth->execute($nombre, $descripcion, $tipo, $precio, $stock, $imagen_ruta);

    print "<h2>Producto agregado exitosamente</h2>";
    print "<a href='script.cgi'>Volver</a>";

} elsif ($accion eq 'actualizar') {
    # Formulario para actualizar stock
    print "<h2>Actualizar Stock</h2>";
    print "<form method='post' action='script.cgi'>";
    print "<input type='hidden' name='accion' value='update'>";
    print "ID del Producto: <input type='number' name='id' required><br>";
    print "Nuevo Stock: <input type='number' name='stock' required><br>";
    print "<input type='submit' value='Actualizar Stock'>";
    print "</form>";

} elsif ($accion eq 'update') {
    # Actualizar stock en la base de datos
    my $id = $cgi->param('id');
    my $stock = $cgi->param('stock');

    my $sth = $dbh->prepare("UPDATE productos SET stock = ? WHERE id = ?");
    $sth->execute($stock, $id);

    print "<h2>Stock actualizado exitosamente</h2>";
    print "<a href='script.cgi'>Volver</a>";

} elsif ($accion eq 'eliminar') {
    # Formulario para eliminar producto
    print "<h2>Eliminar Producto</h2>";
    print "<form method='post' action='script.cgi'>";
    print "<input type='hidden' name='accion' value='delete'>";
    print "ID del Producto: <input type='number' name='id' required><br>";
    print "<input type='submit' value='Eliminar Producto'>";
    print "</form>";

} elsif ($accion eq 'delete') {
    # Eliminar producto de la base de datos
    my $id = $cgi->param('id');

    my $sth = $dbh->prepare("DELETE FROM productos WHERE id = ?");
    $sth->execute($id);

    print "<h2>Producto eliminado exitosamente</h2>";
    print "<a href='script.cgi'>Volver</a>";
}

# Finalizar
print "</body></html>";
$dbh->disconnect;
