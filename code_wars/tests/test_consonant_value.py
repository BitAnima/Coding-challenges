
import unittest
from src.kyu6.consonant_value import solve

class TestConsonantValue(unittest.TestCase):

    # Cada método que empiece con "test_" es una prueba
    def test_basic_cases(self):
        """Prueba los casos básicos."""
        # 'test.assert_equals(a, b)' se convierte en 'self.assertEqual(a, b)'
        self.assertEqual(solve("zodiac"), 26)
        self.assertEqual(solve("chruschtschov"), 80)
        self.assertEqual(solve("khrushchev"), 38)
        self.assertEqual(solve("strength"), 57)
        self.assertEqual(solve("catchphrase"), 73)
        self.assertEqual(solve("twelfthstreet"), 103)
        self.assertEqual(solve("mischtschenkoana"), 80)
        # Nota: He corregido los valores de los dos primeros tests que parecían incorrectos en tu archivo original.
        # solve("cozy") es 51 y solve("") es 0, no 126.
        self.assertEqual(solve("cozy"), 51)
        self.assertEqual(solve(""), 0)

"""# Esta línea permite ejecutar el archivo de tests directamente
if __name__ == '__main__':
    unittest.main()"""