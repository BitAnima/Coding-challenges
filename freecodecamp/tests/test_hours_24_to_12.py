import unittest
from freecodecamp.src.hours_24_to_12 import to_12

class TestHours24to12(unittest.TestCase):
    def test_1(self):
        result = to_12("1124")
        print(" Resultado:", result)
        self.assertEqual(result, "11:24 AM")
    def test_2(self):
        result = to_12("0900")
        print(" Resultado:", result)
        self.assertEqual(result, "9:00 AM")
    def test_3(self):
        result = to_12("1455")
        print(" Resultado:", result)
        self.assertEqual(result, "2:55 PM")
    def test_4(self):
        result = to_12("2346")
        print(" Resultado:", result)
        self.assertEqual(result, "11:46 PM")
    def test_45(self):
        result = to_12("0030")
        print(" Resultado:", result)
        self.assertEqual(result, "12:30 AM")
