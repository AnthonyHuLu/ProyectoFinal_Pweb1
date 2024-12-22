document.getElementById('loginSubmit').addEventListener('click', function() {
    const user = document.getElementById('loginUser').value;
    const password = document.getElementById('loginPassword').value;

    fetch('http://localhost:3000/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: user, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (data.role === 'duenio') {
                if (data.pet_id) {
                    // Redirigir a configuración con el ID de la mascota
                    window.location.href = `configuracion.html?user_id=${data.user_id}&pet_id=${data.pet_id}`;
                } else {
                    // Redirigir a configuración sin el ID de la mascota
                    window.location.href = `configuracion.html?user_id=${data.user_id}`;
                }
            } else if (data.role === 'personal') {
                // Redirigir a la página de menú de personal
                window.location.href = `personal_menu.html?user_id=${data.user_id}`;
            } else {
                alert('Rol desconocido.');
            }
        } else {
            alert('Inicio de sesión fallido: ' + data.message);
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('cancelLogin').addEventListener('click', function() {
    document.getElementById('loginModal').style.display = 'none';
});

document.getElementById('closeLogin').addEventListener('click', function() {
    document.getElementById('loginModal').style.display = 'none';
});

