document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    const loginButton = document.querySelector('.nav-link[href*="auth.login"]');
    const registerButton = document.querySelector('.nav-link[href*="auth.register"]');
    const loginForm = document.querySelector('form[action*="auth.login"]');
    const registerForm = document.querySelector('form[action*="auth.register"]');
    const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
    const paragraphs = document.querySelectorAll('p');
    const images = document.querySelectorAll('img');

    // Animate the navbar
    gsap.from(navbar, {
        duration: 1,
        y: -100,
        opacity: 0,
        ease: 'power4.out'
    });

    // Animate the login button
    gsap.from(loginButton, {
        duration: 1,
        x: -50,
        opacity: 0,
        ease: 'power4.out',
        delay: 0.5
    });

    // Animate the register button
    gsap.from(registerButton, {
        duration: 1,
        x: 50,
        opacity: 0,
        ease: 'power4.out',
        delay: 0.5
    });

    // Animate the login form
    if (loginForm) {
        gsap.from(loginForm, {
            duration: 1,
            y: 50,
            opacity: 0,
            ease: 'power4.out',
            delay: 1
        });
    }

    // Animate the register form
    if (registerForm) {
        gsap.from(registerForm, {
            duration: 1,
            y: 50,
            opacity: 0,
            ease: 'power4.out',
            delay: 1
        });
    }

    // Animate headings
    gsap.from(headings, {
        duration: 1,
        y: 20,
        opacity: 0,
        ease: 'power4.out',
        stagger: 0.2,
        delay: 1.5
    });

    // Animate paragraphs
    gsap.from(paragraphs, {
        duration: 1,
        y: 20,
        opacity: 0,
        ease: 'power4.out',
        stagger: 0.2,
        delay: 2
    });

    // Animate images
    gsap.from(images, {
        duration: 1,
        scale: 0.8,
        opacity: 0,
        ease: 'power4.out',
        stagger: 0.2,
        delay: 2.5
    });
});