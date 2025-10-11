import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.kyu6.find_unique_number import find_uniq

import random
from random import randrange, randint
from collections import Counter




class Test(unittest.TestCase):

    def test_find_uniq_check(self):
        obj = Counter(arr);
        for k, v in obj.items():
            if v == 1: return k


    def test_generate_test_arr(self):
        arr = [mass] * length
        arr[randrange(length)] = answer
        return arr



    def test_basic(self):

        def f():
            self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)
            self.assertEqual(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
            self.assertEqual(find_uniq([3, 10, 3, 3, 3]), 10)


        def f():
            self.assertEqual(find_uniq([4, 4, 4, 3, 4, 4, 4, 4]), 3)
            self.assertEqual(find_uniq([5, 5, 5, 5, 4, 5, 5, 5]), 4)
            self.assertEqual(find_uniq([6, 6, 6, 6, 6, 5, 6, 6]), 5)
            self.assertEqual(find_uniq([7, 7, 7, 7, 7, 7, 6, 7]), 6)


        def f():
            self.assertEqual(find_uniq([8, 8, 8, 8, 8, 8, 8, 7]), 7)
            self.assertEqual(find_uniq([3, 3, 3, 3, 3, 3, 3, 2]), 2)
            self.assertEqual(find_uniq([2, 2, 2, 2, 2, 2, 2, 1]), 1)


        def f():
            self.assertEqual(find_uniq([0, 1, 1, 1, 1, 1, 1, 1]), 0)


        def f():
            self.assertEqual(find_uniq(generate_test_arr(2 ** 40, 2 ** 50, 2 ** 20)), 2 ** 40)


        def f():
            self.assertEqual(find_uniq(generate_test_arr(-1, 1, 1000)), -1)


        def f():
            self.assertEqual(find_uniq(generate_test_arr(0.0000001, 0.0010001, 1000)), 0.0000001)


        def f():
            self.assertEqual(find_uniq(generate_test_arr(42, 24, 2 ** 23)), 42)


        def f():
            from math import inf as infinity
            self.assertEqual(find_uniq(generate_test_arr(-infinity, infinity, 1000)), -infinity)



    def test_rndm(self):

        def f():
            for j in range(5):
                a = randint(2, 10000)
                b = a + randint(2, 5)
                arr = [a] * randint(1, 15) + [b] + [a] * randint(1, 14)
                self.assertEqual(find_uniq(arr), b)


        def f():
            for h in range(20):
                a, b = randint(2, 100000), randint(2, 100000)
                if a == b: continue
                self.assertEqual(find_uniq(generate_test_arr(a, b, 1000)), a)

        
        def f():
            for h in range(20):
                a, b = randint(2, 100000) + random.random(), randint(2, 100000) + random.random()
                if a == b: continue
                self.assertEqual(find_uniq(generate_test_arr(a, b, 1000)), a)

