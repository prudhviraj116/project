$('a[href^="#"]').on('click', function(event) {
    var target = $(this).attr('href');
    $('html, body').stop().animate({
        'scrollTop': $(target).offset().top
    }, 500, 'swing');
    event.preventDefault();
});
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
document.getElementById('profileForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Handle form submission logic here
});
