// select the guess form element by ID
const guessForm = document.getElementById('guessBox')
// adds event listner for the form submission
guessForm.addEventListener('submit', function(e){
    // prevents window from reloading
    e.preventDefault();

    // retreives value from input field
    const guessInput = e.target.elements.guess.value;

    // send the guess to the server using an Axios POST req
    axios.post('/submitGuess', {
        // sends guess as JSON
        guess: guessInput
    })
    .then(response => {
        // gets result from response data
        const result = response.data.result;
        // gets score from response
        const score = response.data.score

        // check the result and alert user accordingly to result
        if (result === 'ok'){
            alert('Valid guess and its on the board!');
            // updates the displayed score
            document.getElementById('scoreValue').innerText = score;
        }
        else if (result === 'not-on-board'){
            alert('Word is valid but not on the board');
        }
        else {
            alert('Not a valid word')
        }
    })
    .catch(error => {
        // handlers any errors that occur during the request
        const errorMessage = error.response?.data.result || 'There was an error';
        // logs the errror
        console.error('There was an error!', errorMessage);
        // alerts error to user
        alert(errorMessage);
    });
    e.target.elements.guess.value = '';
})

// retrieves tghe button to generate the board
const startButton = document.getElementById('generate-board');
startButton.addEventListener('click', function(){
    // gets board table element
    const boardTable = document.getElementById('boardTable')
    // gets guess box element
    const guessBox = document.getElementById('guessBox');
    // gets score box element
    const scoreBox = document.getElementById('scoreBox');

    // toggles visibility of items
    boardTable.style.display = 'block';
    startButton.style.display = 'none';
    guessBox.style.display = 'block';
    scoreBox.style.display = 'block'
});