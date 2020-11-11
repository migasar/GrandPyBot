let dialogBoxElt = document.querySelector('#dialog-box');
let userFormElt = document.querySelector('#user-form');
let userTextElt = document.querySelector('#userText');


function addDialogElt(contentElt, classElt) {
    // Add an element of the bot answer to the main dialog

    let dialogElt = document.createElement('p');
    dialogElt.className = classElt;

    dialogElt.textContent = contentElt;
    dialogBoxElt.appendChild(dialogElt);
}


function addMapElt(answerMap) {
    // Add an element of the bot answer to the main dialog

    let botMap = document.createElement('div');
    botMap.id = 'map';
    botMap.className = 'answer';

    dialogBoxElt.appendChild(botMap);
    initMap(answerMap['latitude'], answerMap['longitude'], 'map')
}


function initMap(placeLatitude, placeLongitude, id) {
    /* Initialize and add the map */

    // Define the location by its coordinates
    let place = { lat: placeLatitude, lng: placeLongitude };
    // Initialized the map, centered on the location
    let map = new google.maps.Map(document.getElementById(id), { zoom: 15, center: place });
    // Add a marker to the map, positioned at the location
    let marker = new google.maps.Marker({ position: place, map: map });
}


function composeAnswer(answerData) {
    /*  Agregate the components of the whole reply from the bot
        depending of the result found to the user question */

    if (answerData['spotted'] == true) {
        // A location has been found

        addDialogElt(answerData['context'], 'answer');
        addDialogElt(`Voici où ton chemin te mène :   ${answerData['address']}`, 'answer');

        addMapElt(answerData);
        addDialogElt(answerData['extract'], 'answer');

    } else {

        addDialogElt(answerData['context'], 'answer');
        addDialogElt(answerData['reply'], 'answer');

    }
}


function postFormData(url, data) {
    // Async function to send the content of the input to the server

    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}


userFormElt.addEventListener('submit', function (event) {
    /* Catch the content of the form sent by the user,
    search for the elements of a response,
    and reply them back to the front. */

    // Avoid to refresh the page
    event.preventDefault();

    // Add the question of the user to the main dialog
    addDialogElt(userTextElt.value, 'question');

    // Send the content of the input to the server
    postFormData("/ask", new FormData(userFormElt))
    .then(data => {
        
        // TEST
        console.log(data);
        
        // Create the answer of the bot
        composeAnswer(data);
    })
})
