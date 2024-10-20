# import statements
from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

# creates an instance for flask app
app = Flask(__name__)
# creates instance for boggle game
boggle_game = Boggle()

# configuration for flask app and debugger
app.config['SECRET_KEY'] = 'Password'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True    
toolbar = DebugToolbarExtension(app)

# load words form the words.txt file into a set for fast lookup
with open('words.txt') as f:
    words = set(f.read().splitlines())

# default home route 
@app.route('/', methods=["POST", "GET"])
def home():
    # call nthe make_method to generate a new board 
    board = boggle_game.make_board() 
    # store the generated board in the session
    session['board'] = board
    # render the home template
    return render_template('home.html', board = board)

# route for submission of guesses
@app.route('/submitGuess', methods = ['POST'])
def submit_guess():
    '''Handle the submission of a guessed word.'''
    # get the guessed word from the request body
    guess = request.json.get('guess')
    # retreive the current board from the session
    board = session.get('board')

    if 'score' not in session:
        session['score'] = 0

    # check if guess is empty and return an error
    if not guess:
        # returns 400 erroor for empty guessed
        return jsonify(result = 'not-a-word'), 400
    
    # check if guessed word is valid
    result = boggle_game.check_valid_word(board, guess)

    # return appropriate responses based on the result 
    if result == 'ok':
        session['score'] += 1
        return jsonify(result = 'ok', score = session['score']), 200
    elif result == 'not-on-board':
        return jsonify(result = 'not-on-board'), 200
    else: 
        return jsonify(result = 'not a word'), 400

# runs the app
if __name__ == '__main__':
    # starts flask app with debug mode enabled
    app.run(debug = True)
