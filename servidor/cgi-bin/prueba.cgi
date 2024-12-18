<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro e Inicio de Sesión</title>
    <script>
        // Validación de coincidencia de contraseñas
        function validarFormulario(e) {
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm_password').value;
            if (password !== confirmPassword) {
                alert('Las contraseñas no coinciden.');
                e.preventDefault();
            }
        }

        // Mostrar modal de registro
        function mostrarRegistro() {
            document.getElementById('registerModal').style.display = 'block';
        }

        // Cerrar modal de registro
        function cerrarRegistro() {
            document.getElementById('registerModal').style.display = 'none';
        }

        // Mostrar modal de inicio de sesión
        function mostrarLogin() {
            document.getElementById('loginModal').style.display = 'block';
        }

        // Cerrar modal de inicio de sesión
        function cerrarLogin() {
            document.getElementById('loginModal').style.display = 'none';
        }

        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('registerSubmit').addEventListener('click', validarFormulario);
            document.getElementById('registerBtn').addEventListener('click', mostrarRegistro);
            document.getElementById('closeRegister').addEventListener('click', cerrarRegistro);
            document.getElementById('cancelRegister').addEventListener('click', cerrarRegistro);
            document.getElementById('loginBtn').addEventListener('click', mostrarLogin);
            document.getElementById('closeLogin').addEventListener('click', cerrarLogin);
            document.getElementById('cancelLogin').addEventListener('click', cerrarLogin);
        });
    </script>
</head>
<body>
    <nav>
        <ul class="menu">
            <li><a href="index.html"><i class="fas fa-comments"></i> Foro</a></li>
            <li><a href="productos.html"><i class="fas fa-shopping-cart"></i> Tienda</a>
                <ul class="submenu">
                    <li><a href="productos.html">Productos</a></li>
                    <li><a href="adopta.html">Adopta</a></li>
                    <li><a href="promo.html">Promos</a></li>
                </ul>
            </li>
            <li><a><i class="fas fa-user"></i> Acceder</a>
                <ul class="submenu">
                    <li><button id="registerBtn">Registrarse</button></li>
                    <li><button id="loginBtn">Iniciar Sesión</button></li>
                </ul>
            </li>
            <li><a href="iniciar_sesion.html"><i class="fas fa-shopping-cart"></i> Eventos</a></li>
            <li><a href="iniciar_sesion.html"><i class="fas fa-phone"></i> Contáctanos</a></li>
            <!-- Barra de búsqueda -->
            <li>
                <div class="search-bar">
                    <input type="text" placeholder="Buscar...">
                    <button><i class="fas fa-search"></i></button>
                </div>
            </li>
        </ul>
    </nav>

    <div class="modal" id="registerModal">
        <div class="modal-content">
            <span class="close" id="closeRegister">&times;</span>
            <h2>Registro de Usuario</h2>
            <form action="/cgi-bin/registro.cgi" method="post">
                <label for="username">Nombre de Usuario:</label><br>
                <input type="text" id="username" name="username" required><br><br>
                <label for="email">Correo Electrónico:</label><br>
                <input type="email" id="email" name="email" required><br><br>
                <label for="password">Contraseña:</label><br>
                <input type="password" id="password" name="password" required minlength="8" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"><br><br>
                <label for="confirm_password">Confirmar Contraseña:</label><br>
                <input type="password" id="confirm_password" name="confirm_password" required><br><br>
                <label for="role">Rol:</label><br>
                <select id="role" name="role" required>
                    <option value="duenio">Dueño</option>
                    <option value="personal">Personal</option>
                    <option value="admin">Admin</option>
                </select><br><br>
                <button type="submit" id="registerSubmit">Registrarse</button>
                <button type="button" id="cancelRegister">Cancelar</button>
            </form>
        </div>
    </div>

    <div class="modal" id="loginModal">
        <div class="modal-content">
            <span class="close" id="closeLogin">&times;</span>
            <h2>Iniciar Sesión</h2>
            <label for="loginUser">Usuario:</label><br>
            <input type="text" id="loginUser" name="loginUser"><br><br>
            <label for="loginPassword">Contraseña:</label><br>
            <input type="password" id="loginPassword" name="loginPassword"><br><br>
            <button class="button" id="loginSubmit">Iniciar Sesión</button>
            <button class="button" id="cancelLogin">Cancelar</button>
        </div>
    </div>
</body>
</html>

