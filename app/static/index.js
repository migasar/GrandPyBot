let dialogBox = document.querySelector('#dialog-container');
let userForm = document.querySelector('#form-container');
let userText = document.querySelector('#userText');


function addDialogElt(contentElt, classElt) {
  /* Add an element to the dialog segment, on the web page. */

  let dialogElt = document.createElement('div');
  dialogElt.className = classElt;
  dialogElt.textContent = contentElt;
  dialogBox.appendChild(dialogElt);
};


function addMapElt(answerMap) {
  /* Add a map object to the dialog segment, on the web page. */

  let botMap = document.createElement('div');
  botMap.className = 'map';
  dialogBox.appendChild(botMap);
  initMap(answerMap['latitude'], answerMap['longitude'], botMap)

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

  if (answerData['spotted'] == true) {
    // Add text
    addDialogElt(answerData['context'], 'answer');
    addDialogElt(answerData['extract'], 'answer');
    // Add the address of the location
    addDialogElt(`Voici où ton chemin te mène :   ${answerData['address']}`, 'answer');
    // Add a map of the location
    addMapElt(answerData);
  } else {
    // Add text
    addDialogElt(answerData['context'], 'answer');
    addDialogElt(answerData['reply'], 'answer');
  }
};

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
}

userForm.addEventListener('submit', function (event) {
  /* 
   * Catch the content of the form sent by the user,
   * search for the elements of a response, and bring them back. 
   */

  // Block the refreshment of the page
  event.preventDefault();

  // Add the question of the user to the main dialog
  addDialogElt(userText.value, 'question');

  // Send the content of the input to the server
  postFormData("/ask", new FormData(userForm))
    .then(data => {
      // Call a function to create the answer of the bot
      composeAnswer(data)
    })
    .catch(error => console.log(error));

  // Clean the input field after settling the user request
  resetInputForm(userForm);
});
