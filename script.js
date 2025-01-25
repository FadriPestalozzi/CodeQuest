// script.js
// Placeholder for future JavaScript functionality

// Add this function to handle language selection
function changeLanguage() {
    const languageSelector = document.getElementById('language');
    languageSelector.onchange = function() {
        window.location.href = this.value;
    };
}

console.log('Welcome to the Youth Hackathon 2025!');