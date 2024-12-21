import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_get_time(self):
        response = self.app.get('/time')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'time', response.data)

if __name__ == '__main__':
    unittest.main()
