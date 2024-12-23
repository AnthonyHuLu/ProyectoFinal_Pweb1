document.getElementById('loginSubmit').addEventListener('click', function() {
    const user = document.getElementById('loginUser').value;
    const password = document.getElementById('loginPassword').value;

    fetch('http://localhost:3000/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: user, password: password }),
        credentials: 'include' // Asegúrate de incluir las credenciales (cookies)
    })
    .then(response => {
        response.json().then(data => {
            if (data.success) {
                console.log('Set-Cookie header:', response.headers.get('Set-Cookie')); // Mostrar la cabecera Set-Cookie
                if (data.role === 'duenio') {
                    window.location.href = `configuracion.html?user_id=${data.user_id}`;
                } else if (data.role === 'personal') {
                    window.location.href = `personal_menu.html?user_id=${data.user_id}`;
                } else {
                    alert('Rol desconocido.');
                }
            } else {
                alert('Inicio de sesión fallido: ' + data.message);
            }
        });
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('cancelLogin').addEventListener('click', function() {
    document.getElementById('loginModal').style.display = 'none';
});

document.getElementById('closeLogin').addEventListener('click', function() {
    document.getElementById('loginModal').style.display = 'none';
});

