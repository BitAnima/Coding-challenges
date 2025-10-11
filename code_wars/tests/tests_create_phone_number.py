import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from src.kyu6.create_phone_number import create_phone_number

class Test(unittest.TestCase):
    def test_fixed(self):

        def basic_test_cases():
            test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
            test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
            test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
            test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
            test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")


        def _():
            from random import randint

            create_sol = lambda n: "(%s) %s-%s" % ("".join(map(str, n[:3])), "".join(map(str, n[3:6])),
                                                   "".join(map(str, n[6:])))

            for _ in range(40):
                n = [randint(0, 9) for qu in range(10)]
                expected = create_sol(n)
                test.assert_equals(create_phone_number(n), expected, f'Testing for {repr(n)}')