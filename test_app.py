import unittest
from app import get_message


class TestApp(unittest.TestCase):
    def test_message(self):
        self.assertEqual(
            get_message(),
            "DVP Week 12 CI/CD Pipeline is running!"
        )


if __name__ == "__main__":
    unittest.main()
