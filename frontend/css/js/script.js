let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 7000); // Cambia de imagen cada 7 segundos
}

function plusSlides(n) {
    slideIndex += n - 1;
    showSlides();
}

document.getElementById('cargar-mas-btn').addEventListener('click', function() {
    let hiddenItems = document.querySelectorAll('.producto-item.hidden');
    hiddenItems.forEach(function(item) {
        item.classList.remove('hidden');
    });
    this.style.display = 'none'; // Ocultar el bot  n despu  s de cargar m  s
});

function obtenerProductos() {
    fetch('http://localhost:3000/api/productos')
        .then(response => response.json())
        .then(data => {
            mostrarProductos(data);
        })
        .catch(error => console.error('Error al obtener productos:', error));
}

function mostrarProductos(productos) {
    const galeria = document.querySelector('.productos-galeria');
    productos.forEach(producto => {
        const productoItem = document.createElement('div');
        productoItem.classList.add('producto-item');
        const imagen = document.createElement('img');
        imagen.src = producto.imagen_ruta;
        imagen.alt = `Producto ${producto.nombre}`;
        const nombre = document.createElement('p');
        nombre.textContent = producto.nombre;
        const precio = document.createElement('p');
        precio.textContent = `$${producto.precio.toFixed(2)}`;
        productoItem.appendChild(imagen);
        productoItem.appendChild(nombre);
        productoItem.appendChild(precio);
        galeria.appendChild(productoItem);
    });
}

document.addEventListener('DOMContentLoaded', obtenerProductos);

document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch('http://localhost:8000/cgi-bin/registro.cgi', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Puedes agregar lógica para mostrar un mensaje de éxito o manejar los errores.
        console.log(data);
        // Redirigir al usuario a la página de configuración de cuenta
        window.location.href = 'http://localhost:8080/configuracion_cuenta.html';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

