
import unittest
import app

class TestApplication(unittest.TestCase):

    def test_server_port(self):
        self.assertEqual(app.PORT, 5000)

    def test_server_address(self):
        self.assertEqual(app.HOST, "0.0.0.0")

if __name__ == "__main__":
    unittest.main()
