document.addEventListener('DOMContentLoaded', () => {
    // Sidebar link click event
    document.querySelectorAll('.sidebar a').forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const target = event.target.dataset.target;
            document.querySelectorAll('.content-section').forEach(section => {
                section.style.display = 'none';
            });
            document.getElementById(target).style.display = 'block';
        });
    });

    // Dropdown buttons
    document.getElementById('add-student').addEventListener('click', () => {
        document.getElementById('popup-form').style.display = 'flex';
    });

    // Close button functionality
    document.querySelector('.close-btn').addEventListener('click', () => {
        document.getElementById('popup-form').style.display = 'none';
    });

    // Handle form submission
    document.getElementById('form').addEventListener('submit', (event) => {
        event.preventDefault();
        alert('Form submitted!');
        document.getElementById('popup-form').style.display = 'none';
    });
});
