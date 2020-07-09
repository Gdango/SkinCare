from app import app
import unittest
from unittest.mock import Mock

class FlaskApp(unittest.TestCase):
    # test response is 200
    def test_index(self):
        apps = app.test_client()
        response = apps.get('/')
        self.assertEqual(response.status_code, 200)

    '''def test_valid_query(self):
        mock_query = Mock()
        mock_query.app.Query.assert_called_with("Combination", 3, '25-to-70')'''



    # test "info" returns the right table

    # test result 
    

if __name__ == "__main__":
    unittest.main()

    

