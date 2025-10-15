import unittest
from freecodecamp.src.hex_to_decimal import hex_to_decimal

class TestHexToDecimal(unittest.TestCase):
    def test_hex_to_decimalA(self):
        result = hex_to_decimal("A")
        print(" Resultado:", result)
        self.assertEqual(result, 10)

    def test_hex_to_decimal15(self):
        result = hex_to_decimal("15")
        print(" Resultado:", result)
        self.assertEqual(result, 21)

    def test_hex_to_decimal2E(self):
        result = hex_to_decimal("2E")
        print(" Resultado:", result)
        self.assertEqual(result, 46)

    def test_hex_to_decimal2E(self):
        result = hex_to_decimal("FF")
        print(" Resultado:", result)
        self.assertEqual(result, 255)

    def test_hex_to_decimal2E(self):
        result = hex_to_decimal("A3F")
        print(" Resultado:", result)
        self.assertEqual(result, 2623)
