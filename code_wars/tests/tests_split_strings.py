import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from src.kyu6.split_strings import solution

class Test(unittest.TestCase):
    def test_fixed(self):

        def test_basic():
            tests = (
                ("asdfadsf", ['as', 'df', 'ad', 'sf']),
                ("asdfads", ['as', 'df', 'ad', 's_']),
                ("", []),
                ("x", ["x_"]),
            )

            for inp, exp in tests:
                self.assertEqual(solution(inp), exp)


    def test_random(self):

        from random import randint, choice
        from string import ascii_lowercase

        reference = lambda s, n=2: [''.join(e) for e in zip(*[iter(s + ['', '_'][len(s) % 2])] * 2)]

        for _ in range(100):
            test_case = "".join(choice(ascii_lowercase) for _ in range(randint(0, 100)))


            def _():
                sol = reference(test_case)
                user = solution(test_case)
                self.assertEqual(user, sol)