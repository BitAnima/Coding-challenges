import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from src.kyu6.replace_with_alphabet_position import alphabet_position


from string import ascii_lowercase as LOW, ascii_uppercase as UP, digits as D, punctuation as PUNC
from random import choice, randint

class Test(unittest.TestCase):


    def ap(text):
        text = text.lower().strip()
        return " ".join([str(ord(x) - ord("a") + 1) for x in text if x in LOW + UP])


    
    def test_fixed(self):
        
        def basic_test_cases():
            self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."),
                               "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
            self.assertEqual(alphabet_position("The narwhal bacons at midnight."),
                               "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

        
        def test_fixed(self):
            self.assertEqual(alphabet_position("-.-'"), "")


        def test_fixed(self):
            for letter in LOW:
                self.assertEqual(alphabet_position(letter), ap(letter))


    
    def test_random(self):
        S = LOW + UP + D + PUNC
        for _ in range(100):
            x = ''.join(choice(S) for _ in range(randint(1, 100)))


            def _():
                self.assertEqual(alphabet_position(x), ap(x))