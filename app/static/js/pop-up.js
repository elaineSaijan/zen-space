// Show the popup when the page loads
window.addEventListener('load', () => {
    const popup = document.getElementById('popup');
    const mainContent = document.getElementById('mainContent');
    popup.style.display = 'block';
    mainContent.classList.add('blurred'); // Add blur effect
});

// Hide the popup when the "Accept" button is clicked
const acceptButton = document.getElementById('acceptButton');
acceptButton.addEventListener('click', () => {
    const popup = document.getElementById('popup');
    const mainContent = document.getElementById('mainContent');
    popup.style.display = 'none';
    mainContent.classList.remove('blurred'); // Remove blur effect
});
