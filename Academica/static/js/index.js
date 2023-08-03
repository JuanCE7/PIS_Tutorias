const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener('click', ()=>{
   //Animate Links
    navLinks.classList.toggle("open");
    links.forEach(link => {
        link.classList.toggle("fade");
    });

    //Hamburger Animation
    hamburger.classList.toggle("toggle");
});


document.getElementById("ingresar-btn").addEventListener("click", function(event) {
    event.preventDefault();  // Evita que se realice la acción por defecto del enlace

    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");

    if (email.trim() === '' || password.trim() === '') {
        errorMessage.textContent = "Por favor, complete todos los campos.";
    } else {
        // Realizar aquí la lógica para enviar el formulario si los campos son válidos
        // Por ejemplo, redirigir a la página de inicio de sesión con los datos del formulario
        window.location.href = "inicio?email=" + encodeURIComponent(email) + "&password=" + encodeURIComponent(password);
    }
});