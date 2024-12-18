document.getElementById('registroMascotaForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const nombreMascota = document.getElementById('nombreMascota').value;
    const tipoMascota = document.getElementById('tipoMascota').value;
    const correoDuenio = document.getElementById('correoDuenio').value;
    const contrasenaDuenio = document.getElementById('contrasenaDuenio').value;

    fetch('/cgi-bin/registro_mascota.cgi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            nombreMascota: nombreMascota,
            tipoMascota: tipoMascota,
            correoDuenio: correoDuenio,
            contrasenaDuenio: contrasenaDuenio,
        })
    })
    .then(response => response.text())
    .then(data => {
        // Manejar la respuesta del servidor
        alert(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

