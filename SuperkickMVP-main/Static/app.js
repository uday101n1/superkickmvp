// Initialize the form and container
//Initialze
const form = document.getElementById("submitForm");
const cardsContainer = document.getElementById("cardsContainer");
let currentSubmissionId = null;

// Handle form submission
form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        iam_input: document.getElementById("iam").value,
        looking_for: document.getElementById("lookingFor").value,
        email: document.getElementById("email").value,
    };

    const response = await fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    //alert(result.message);
    form.reset();
    loadSubmissions();  // Reload submissions after a successful submit
});

async function loadSubmissions() {
    const response = await fetch("http://127.0.0.1:5000/get_submissions");
    const submissions = await response.json();
    const cardsContainer = document.getElementById('cardsContainer');

    // Clear existing content
    cardsContainer.innerHTML = "";

    submissions.forEach((sub) => {
        const card = document.createElement("li");
        card.className = "member co-funder";
        const imageCount = 17; // Number of images in your folder
        const randomImageIndex = Math.floor(Math.random() * imageCount) + 1;
        const randomImagePath = `/static/images/image${randomImageIndex}.png`;
        card.innerHTML = `
            <div class="thumb"><img src="${randomImagePath}" alt="User avatar"></div>
            <div class="description">
                <h3>${sub.name}</h3>
                <p>I am <strong>${sub.iam_input}</strong>, looking for someone <strong>${sub.looking_for}</strong><br>
                <button class="btn-open-popup" data-submission-id="${sub.id}">Join them</button></p>
            </div>
        `;
        
        // Attach the card to the container
        cardsContainer.appendChild(card);
    });

    // Attach event listeners to buttons dynamically
    document.querySelectorAll('.btn-open-popup').forEach(button => {
        button.addEventListener('click', (e) => {
            const submissionId = e.target.getAttribute('data-submission-id');
            openPopup(submissionId);  // Open the popup with the submission ID
        });
    });
}


// Open the popup and set the current submission ID
function openPopup(submissionId) {
    currentSubmissionId = submissionId;  // Set currentSubmissionId
    console.log(`Popup opened for submission ID: ${submissionId}`);  // Debug log
    document.getElementById("popup").style.display = "block";  // Show the popup
    document.getElementById("popupOverlay").classList.add('show');  // Show overlay
}

// Close the popup
function closePopup() {
    document.getElementById("popup").style.display = "none";  // Hide the popup
    document.getElementById("popupOverlay").classList.remove('show');  // Hide overlay
}
document.addEventListener("DOMContentLoaded", () => {
document.getElementById("joinSubmit").addEventListener("click", async () => {
    console.log("Button clicked");
    // Get data from form fields
    const data = {
        submission_id: currentSubmissionId,  // Correct syntax for property assignment
        name: document.getElementById("joinName").value,
        social_media: document.getElementById("joinSocial").value,
        email: document.getElementById("joinEmail").value,
    };

    // Make the fetch request to the server
    const response = await fetch("http://127.0.0.1:5000/join", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });


    // Handle the response
    const result = await response.json();
    alert(result.message);  // Show the result message

    // Close the popup and reload submissions
    
});
});

// Load submissions when the page loads
loadSubmissions();

document.addEventListener('DOMContentLoaded', function() {
    const scrollToTopLinks = document.querySelectorAll('.navbar-logo a, .navbar-title a');

    scrollToTopLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    });
});
