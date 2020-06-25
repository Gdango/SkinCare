from app import app
import unittest

class FlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # test response is 200
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    '''def test_valid_query(self):
        query_result = self.app.Query('Combination', '4', '25-to-70')
        response = self.app.get('/Result')
        self.assertEqual(response.status_code, 200)'''

    # test "info" returns the right table

    # test result 
    

if __name__ == "__main__":
    unittest.main()

    

