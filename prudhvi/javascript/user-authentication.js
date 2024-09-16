
document.addEventListener("DOMContentLoaded", function() {
    // Get the form element
    const form = document.querySelector("form");

    // Add event listener for form submission
    form.addEventListener("submit", function(event) {
        // Prevent the default form submission
        event.preventDefault();

        // Get the username and password entered by the user
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // Perform simple validation (you can add more robust validation)
        if (username === "admin" && password === "password") {
            // If credentials are correct, redirect to the main page
            window.location.href = "royalenfield.html";
        } else {
            // If credentials are incorrect, display an error message
            alert("Invalid username or password. Please try again.");
        }
    });
});
