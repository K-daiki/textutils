# tests/test_counter.py

import unittest
from textutils.counter import count_words

class TestCounter(unittest.TestCase):
    def test_word_count(self):
        text = "This is a sample sentence. This sentence is for testing word count."
        expected_word_count = {'This': 2, 'is': 2, 'a': 1, 'sample': 1, 'sentence': 2, 'for': 1, 'testing': 1, 'word': 1, 'count': 1}
        word_count = count_words(text)
        self.assertEqual(word_count, expected_word_count)

if __name__ == '__main__':
    unittest.main()
