// script.js

var rainbowColors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#8B00FF'];
var currentColorIndex = 0;

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
