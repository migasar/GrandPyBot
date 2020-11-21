let dialogBox = document.querySelector('#dialog-container');
let userForm = document.querySelector('#form-container');


// Catch the content of the form sent by the user, and bring back a response
userForm.addEventListener('submit', function (event) {
  // Block the refreshment of the page
  event.preventDefault();

  // Launch loading animation
  runLoadAnimation();
  // Add the question of the user to the main dialog
  let userText = document.querySelector('#userText');
  addDialogElt(dialogBox, userText.value, 'question');

  // Send the content of the input to the server
  postFormData('/ask', new FormData(userForm))
    .then(data => {
      // Call a function to create the answer of the bot
      composeAnswer(data)
    })
    .catch(error => console.log(error));

  // Clean the input field after settling the user request
  resetInputForm(userForm);
});


// Async function to send the content of the input to the server
function postFormData(url, data) {
  return fetch(url, {
      method: "POST",
      body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
};


// Agregate the components of the whole reply from the bot
function composeAnswer(answerData) {
  // Create an object to contain the components of the answer
  let answerContainer = document.createElement('div');
  answerContainer.className = 'answer';

  // Pile the components of the answer in their container
  if (answerData['spotted'] == true) {
    // Add the address of the location
    addDialogElt(answerContainer, answerData['reply'], 'result');
    addDialogElt(answerContainer, answerData['address'], 'address');
    // Add text
    addDialogElt(answerContainer, answerData['context'], 'context');
    addDialogElt(answerContainer, answerData['extract'], 'extract');
    // Add a map of the location
    let botMap = document.createElement('div');
    botMap.className = 'map';
    answerContainer.appendChild(botMap);
    initMap(answerData['latitude'], answerData['longitude'], botMap);
  } else {
    // Add text
    addDialogElt(answerContainer, answerData['reply'], 'result');
    addDialogElt(answerContainer, answerData['context'], 'context');
  };

  // Append the answer object to the dialog segment on the html
  dialogBox.appendChild(answerContainer);
  // Ensure that the dialog section scrolls from the bottom by default
  answerContainer.scrollIntoView();
};


// Add an element to the dialog segment, on the web page
function addDialogElt(containerElt, contentElt, classElt) {
  let dialogElt = document.createElement('div');
  dialogElt.className = classElt;
  dialogElt.textContent = contentElt;
  containerElt.appendChild(dialogElt);
};


// Initialize a map object
function initMap(placeLatitude, placeLongitude, div) {
  // Define the location by its coordinates
  let place = {
    lat: placeLatitude,
    lng: placeLongitude
  };
  // Initialize the map, centered on the location
  let map = new google.maps.Map(div, {
    zoom: 15,
    center: place
  });
  // Add a marker to the map, positioned at the location
  let marker = new google.maps.Marker({
    position: place,
    map: map
  });
};


// Spin the image of the button
function runLoadAnimation() {
  // Launch loading animation
  let inputImage = document.querySelector('#inputImage');
  inputImage.classList.add('spinning');
  // Stop the animation after a fixed time interval
  setTimeout(() => inputImage.classList.remove('spinning'), 2000);
};


// Remove the user request from the input field
function resetInputForm(docElt) {
  docElt.reset();
};
