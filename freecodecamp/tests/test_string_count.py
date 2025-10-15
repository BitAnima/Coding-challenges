import unittest
from freecodecamp.src.string_count import count

class Teststringcount(unittest.TestCase):
    def test_1(self):
        result = count('abcdefg', 'def')
        print(" Resultado:", result)
        self.assertEqual(result, 1)
    def test_2(self):
        result = count('hello', 'world')
        print(" Resultado:", result)
        self.assertEqual(result, 0)
    def test_3(self):
        result = count('mississippi', 'iss')
        print(" Resultado:", result)
        self.assertEqual(result, 2)
    def test_4(self):
        result = count('she sells seashells by the seashore', 'sh')
        print(" Resultado:", result)
        self.assertEqual(result, 3)
    def test_5(self):
        result = count('101010101010101010101', '101')
        print(" Resultado:", result)
        self.assertEqual(result, 10)

