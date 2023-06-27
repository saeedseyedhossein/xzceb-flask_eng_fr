import unittest
from translator import english_to_french, french_to_english

class TestTrans(unittest.TestCase):
    def test_etf(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
    
    def test_fte(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()