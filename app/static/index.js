let dialogBox = document.querySelector('#dialog-container');
let userForm = document.querySelector('#form-container');


function postFormData(url, data) {
  /* Async function to send the content of the input to the server */
  return fetch(url, {
      method: "POST",
      body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
};

function resetInputForm(docElt) {
  /* Remove the user request from the input field */
  docElt.reset();
};

function runLoadAnimation() {
  // Launch loading animation
  let inputImage = document.querySelector('#inputImage');
  inputImage.classList.add('spinning');
  // Stop the animation after a fixed time interval
  setTimeout(() => inputImage.classList.remove('spinning'), 2000);
};

function addDialogElt(containerElt, contentElt, classElt) {
  /* Add an element to the dialog segment, on the web page. */
  let dialogElt = document.createElement('div');
  dialogElt.className = classElt;
  dialogElt.textContent = contentElt;
  containerElt.appendChild(dialogElt);
};

function initMap(placeLatitude, placeLongitude, div) {
  /* Initialize a map object. */
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

function composeAnswer(answerData) {
  /*  
   * Agregate the components of the whole reply from the bot, 
   * depending of the result found to the user question. 
   */

  // Create an object to contain the components of the answer
  let answerContainer = document.createElement('div');
  answerContainer.className = 'answer';

  // Pile the components of the answer in their container
  if (answerData['spotted'] == true) {
    // Add the address of the location
    addDialogElt(answerContainer, `Voici où ton chemin te mène :`, 'result');
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

userForm.addEventListener('submit', function (event) {
  /* 
   * Catch the content of the form sent by the user,
   * search for the elements of a response, and bring them back. 
   */

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
