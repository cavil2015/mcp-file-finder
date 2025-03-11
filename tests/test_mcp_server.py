import unittest
from mcp_server import app

class TestMCPServer(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_find_files_with_query(self):
        response = self.client.get('/find?query=test')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_find_files_without_query(self):
        response = self.client.get('/find')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)

if __name__ == '__main__':
    unittest.main()