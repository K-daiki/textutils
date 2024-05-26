# tests/test_tokenizer.py

import unittest
from textutils.tokenizer import tokenize

class TestTokenizer(unittest.TestCase):
    def test_tokenization(self):
        text = "This is a sample sentence for testing tokenization."
        expected_tokens = ["This", "is", "a", "sample", "sentence", "for", "testing", "tokenization"]
        tokens = tokenize(text)
        self.assertEqual(tokens, expected_tokens)

if __name__ == '__main__':
    unittest.main()
