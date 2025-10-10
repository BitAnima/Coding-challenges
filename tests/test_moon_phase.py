"""
Tests automáticos para el módulo moon_phase.py.


Para ejecutar los tests:
    python -m unittest moon_phase.py
"""

import unittest
from src.moon_phase import moon_phase

class TestLandingSpot(unittest.TestCase):
    def test_new_moon(self):
        """moon_phase("2000-01-12") # "New"."""
        result = moon_phase("2000-01-12")
        print(" Resultado test_new_moon:", result)
        self.assertEqual(result, "New")

        def test_waxing(self):
            """moon_phase("2000-01-13") # "Waxing"""
            result = moon_phase("2000-01-13")
            print(" Resultado test_waxing:", result)
            self.assertEqual(result, "Waxing")

        def test_full(self):
            """moon_phase("2014-10-15") # "Full"""
            result = moon_phase("2014-10-15")
            print(" Resultado test_full:", result)
            self.assertEqual(result, "Full")

        def test_waning(self):
            """moon_phase("2012-10-21") # "Waning"""
            result = moon_phase("2012-10-21")
            print(" Resultado test_waning:", result)
            self.assertEqual(result, "Waning")


        # moon_phase("2022-12-14")        # "New".

if __name__ == '__main__':
    unittest.main()