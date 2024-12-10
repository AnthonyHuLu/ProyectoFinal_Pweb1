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

