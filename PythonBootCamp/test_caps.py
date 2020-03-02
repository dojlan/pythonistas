import unittest
import caps_file

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = caps_file.cap_func(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = caps_file.cap_func(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()