// main.js

// Document ready function
document.addEventListener("DOMContentLoaded", function() {
    // Example: Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('.navbar-nav a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Example: Alert when a button is clicked
    const alertButton = document.getElementById('alert-button');
    if (alertButton) {
        alertButton.addEventListener('click', function() {
            alert('Button clicked!');
        });
    }

    // Example: Toggle a class on the navbar when scrolling
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
});
