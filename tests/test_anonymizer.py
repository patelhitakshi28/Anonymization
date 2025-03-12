import unittest
from src.anonymizer import anonymize_message

class TestAnonymizer(unittest.TestCase):
    def test_anonymize_message(self):
        message = "Hello, my name is Alice."
        anonymized = anonymize_message(message)
        self.assertNotIn("Alice", anonymized)
        self.assertNotEqual(message, anonymized)

if __name__ == "__main__":
    unittest.main()