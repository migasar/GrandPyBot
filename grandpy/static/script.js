let dialogBoxElt = document.querySelector("#dialog-box");
let userFormElt = document.querySelector("#user-form");
let userTextElt = document.querySelector("#userText");


function addQuestionElt(questionText) {
    // Add the question of the user to the main dialog

    let userQuestion = document.createElement("p");
    userQuestion.className = "question";

    userQuestion.textContent = questionText;
    dialogBoxElt.append(userQuestion);
}

function addAnswerElt(answerText) {
    // Add an element of the bot answer to the main dialog

    let botAnswer = document.createElement("p");
    botAnswer.className = "answer";

    botAnswer.textContent = answerText;
    dialogBoxElt.append(botAnswer);
}

function composeAnswer(answerData) {
    /*  Agregate the components of the whole reply from the bot 
        depending of the result found to the user question */

    if (answerData["spotted"] == true) {
        // A location has been found
        addAnswerElt("Spotted");
        addAnswerElt(answerData["context"]);
        addAnswerElt(answerData["extract"]);
        addAnswerElt(answerData["latitude"]);
        addAnswerElt(answerData["longitude"]);
    } else {
        addAnswerElt("Lost");
        addAnswerElt(answerData["context"]);
        addAnswerElt(answerData["reply"]);
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

userFormElt.addEventListener("submit", function (event) {
    /* Catch the content of the form sent by the user,
    search for the elements of a response,
    and reply them back to the front. */

    // Avoid to refresh the page
    event.preventDefault();

    // Add the question of the user to the main dialog
    addQuestionElt(userTextElt.value);

    // Send the content of the input to the server
    postFormData("/ask", new FormData(userFormElt))
    .then(data => {
        // Create the answer of the bot
        composeAnswer(data);
    })
})
