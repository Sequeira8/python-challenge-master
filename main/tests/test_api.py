'''Tests for the api.py file'''

import unittest

import sys
sys.path.append("..")
from api import app


class TestApi(unittest.TestCase):
    '''Testing api'''


    def setUp(self):
        '''Sets up app to be tested'''

        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        '''Tests if the status on the main page returns sucess'''

        # sends HTTP GET request to the application
        #on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
