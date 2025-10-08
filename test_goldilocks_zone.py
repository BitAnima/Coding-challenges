"""
Tests automáticos para el módulo goldilocks_zone.py.

Se valida que la función goldilocks_zone devuelve los rangos correctos
de la zona Goldilocks para distintas masas estelares, así como el correcto
manejo de errores para valores inválidos.

Para ejecutar los tests:
    python -m unittest test_goldilocks_zone.py
"""


import unittest
from goldilocks_zone import goldilocks_zone

class TestGoldilocksZone(unittest.TestCase):
    """
        Casos de prueba para la función goldilocks_zone.
        """

    """def test_sol(self):
        self.assertEqual(goldilocks_zone(1), [0.95, 1.37])"""

    def test_sol(self):
        result = goldilocks_zone(1)
        print(" Resultado test_sol:", result)
        self.assertEqual(result, [0.95, 1.37])

    def test_menor_que_1(self):
        self.assertEqual(goldilocks_zone(0.5), [0.28, 0.41])

    def test_masivo(self):
        self.assertEqual(goldilocks_zone(6), [21.85, 31.51])

    def test_error_cero(self):
        with self.assertRaises(ValueError):
            goldilocks_zone(0)

    def test_error_negativo(self):
        with self.assertRaises(ValueError):
            goldilocks_zone(-1)
