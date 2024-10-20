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


if __name__ == '__main__':
    unittest.main()