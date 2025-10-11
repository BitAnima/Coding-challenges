import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from src.kyu5.first_non_repeating import first_non_repeating_letter

class Test(unittest.TestCase):
    def test_fixed(self):

        def _():
           self.assertEqual(first_non_repeating_letter('a'), 'a')
           self.assertEqual(first_non_repeating_letter('stress'), 't')
           self.assertEqual(first_non_repeating_letter('moonmen'), 'e')


        def _():
           self.assertEqual(first_non_repeating_letter(''), '')


        def _():
           self.assertEqual(first_non_repeating_letter('abba'), '')
           self.assertEqual(first_non_repeating_letter('aa'), '')


        def _():
           self.assertEqual(first_non_repeating_letter('~><#~><'), '#')
           self.assertEqual(first_non_repeating_letter('hello world, eh?'), 'w')


        def _():
           self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')
           self.assertEqual(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')


    def test_random(self):
        import random
        from collections import Counter

        class Letter(tuple):
            def __hash__(self): return ord(self[0])

            def __eq__(self, other): return self[0] == other[0]

        def ref_sol(s):
            letters = Counter([Letter((c.lower(), c)) for c in s])
            for k, count in letters.items():
                if count == 1:
                    return k[1]
            return ""

        base = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789;,:."

        for _ in range(50):
            sample = random.choices(base, k=random.randint(10, 60))
            if random.randint(0, 10) < 4:
                half = sample[:len(sample) // 2]
                sample = half + half
            random.shuffle(sample)
            s = "".join(sample)


            def _():
                expected = ref_sol(s)
                actual = first_non_repeating_letter(s)
                self.assertEqual(actual, expected)