# import statements
from boggle import Boggle
from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
boggle_game = Boggle()

# enables debugtoolbar
app.config['SECRET_KEY'] = 'Password'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True    
toolbar = DebugToolbarExtension(app)

# default home route 
@app.route('/', methods=["POST", "GET"])
def home():
    # calls make board func from boggle.py
    board = boggle_game.make_board() 
    session['board'] = board
    return render_template('home.html', board = board)


if __name__ == '__main__':
    app.run(debug = True)
