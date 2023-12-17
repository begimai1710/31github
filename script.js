// script.js

var rainbowColors = ['#FF69B4', '#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#8B00FF'];

var currentColorIndex = 1; // Start with index 1 for pink

function changeHeaderColor() {
    // Access the element with the id 'header'
    var headerElement = document.getElementById("header");

    // Change the background color of the header to the next rainbow color
    headerElement.style.backgroundColor = getNextRainbowColor();
}

function getNextRainbowColor() {
    // Get the next rainbow color from the array
    var nextColor = rainbowColors[currentColorIndex];

    // Increment the index for the next function call
    currentColorIndex = (currentColorIndex + 1) % rainbowColors.length;

    return nextColor;
}
