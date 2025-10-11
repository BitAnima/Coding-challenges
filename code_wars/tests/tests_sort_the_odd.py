import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from src.kyu6.sort_the_odd import sort_array


class Test(unittest.TestCase):
    def test_fixed(self):

        def basic_test_cases():
           self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
           self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
           self.assertEqual(sort_array([]), [])
           self.assertEqual(sort_array([5, 3, 2, 8, 1, 4, 11]), [1, 3, 2, 8, 5, 4, 11])
           self.assertEqual(sort_array([2, 22, 37, 11, 4, 1, 5, 0]), [2, 22, 1, 5, 4, 11, 37, 0])
           self.assertEqual(sort_array([1, 111, 11, 11, 2, 1, 5, 0]), [1, 1, 5, 11, 2, 11, 111, 0])
           self.assertEqual(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
           self.assertEqual(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
           self.assertEqual(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]), [0, 1, 2, 3, 4, 5, 8, 7, 6, 9])


    def test_random(self):
        import random
        def reference(a):
            odd = sorted((x for x in a if x % 2), reverse=True)
            return [odd.pop() if x % 2 else x for x in a]

        for _ in range(100):
            a = random.choices(range(-50, 51), k=random.randint(0, 30))
            result = reference(a[:])

            
            def test_basic_tests():
               self.assertEqual(sort_array(a[:]), result)