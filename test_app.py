import unittest
from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    # TODO -- write tests for every view function / feature!

    def setUp(self):
        '''Set up a test client.'''
        self.app = app 
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_home_route(self):
        '''Test that the home route generates a Boggle board and returns a 200 status code.'''
        
        response = self.client.get('/')

        # check if the status code is 200
        self.assertEqual(response.status_code, 200)

        # check if the board is in the session
        with self.client:
            self.client.get('/')
            self.assertIn('board', session)

            # checks if board is a 5x5 grid
            board = session['board']
            # checks for 5 rows
            self.assertEqual(len(board), 5) 
            for row in board: 
                # checks for 5 columns in each row
                self.assertEqual(len(row), 5)

    def get_valid_word_from_board(self, board):
        """This function gets a valid word for the following test cases"""
        for row in board:
            for letter in row:
                # Let's just return a single letter for the sake of the test
                # Replace this logic with your actual valid word selection
                return letter
        return "INVALID"
    
    def test_submit_guess_valid_word(self):
        '''Test submitting a valid guess that is a word.'''

        with self.client:
            # First generate a board
            response = self.client.get('/')
            board = session['board']

            # Choose a word from the board for testing
            valid_word = self.get_valid_word_from_board(board)

            # Submit the valid word
            response = self.client.post('/submitGuess', json={'guess': valid_word})
            self.assertEqual(response.status_code, 200)
            
            # Check that the response indicates the word is valid
            self.assertEqual(response.json['result'], 'ok')
            # Check that the score has been updated
            self.assertEqual(session['score'], 1)
    
    def test_submit_invalid_guess_not_a_word(self):
        '''Test submuitting an invalid guess that is not a word.'''

        with self.client:
            self.client.get('/')
            response = self.client.post('/submitGuess', json = {'guess': 'jnvjen'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json['result'], 'not a word')

    def test_submit_valid_guess_not_on_board(self):
        '''Test submitting a valud word that is not on the board.'''

        with self.client:
            self.client.get('/')
            response = self.client.post('/submitGuess', json = {'guess': 'word'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['result'], 'not-on-board')

if __name__ == '__main__':
    unittest.main()