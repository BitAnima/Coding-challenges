"""
Tests automáticos para Space Week Day 4: Landing Spot.

Verifica que la función find_landing_spot(local_map) devuelva correctamente
la posición [fila, columna] del landing spot más seguro, según los ejemplos del reto.

Coloca este archivo en la carpeta 'tests/' y ejecuta con:
    python -m unittest discover -s tests
"""

import unittest
from freecodecamp.src.landing_spot import find_landing_spot

class TestLandingSpot(unittest.TestCase):
    def test_caso_1(self):
        """find_landing_spot([[1, 0], [2, 0]]) debería devolver [0, 1]."""
        mapa = [
            [1, 0],
            [2, 0]
        ]
        self.assertEqual(find_landing_spot(mapa), [0, 1])

    def test_caso_2(self):
        """find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) debería devolver [1, 1]."""
        mapa = [
            [9, 0, 3],
            [7, 0, 4],
            [8, 0, 5]
        ]
        self.assertEqual(find_landing_spot(mapa), [1, 1])

    def test_caso_3(self):
        """find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) debería devolver [2, 2]."""
        mapa = [
            [1, 2, 1],
            [0, 0, 2],
            [3, 0, 0]
        ]
        self.assertEqual(find_landing_spot(mapa), [2, 2])

    def test_caso_4(self):
        """find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) debería devolver [2, 1]."""
        mapa = [
            [9, 6, 0, 8],
            [7, 1, 1, 0],
            [3, 0, 3, 9],
            [8, 6, 0, 9]
        ]
        self.assertEqual(find_landing_spot(mapa), [2, 1])

if __name__ == '__main__':
    unittest.main()
