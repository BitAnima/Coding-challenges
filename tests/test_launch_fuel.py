import unittest
from src.launch_fuel import launch_fuel

class TestLaunchFuel(unittest.TestCase):
    def test_caso_1(self):
        result = launch_fuel(50)
        print(" Resultado:", result)
        self.assertEqual(launch_fuel(50), 12.4)

    def test_caso_2(self):
        result = launch_fuel(500)
        print(" Resultado:", result)
        self.assertEqual(launch_fuel(500), 124.8)

    def test_caso_3(self):
        result = launch_fuel(243)
        print(" Resultado:", result)
        self.assertEqual(launch_fuel(243), 60.7)

    def test_caso_4(self):
        result = launch_fuel(11000)
        print(" Resultado:", result)
        self.assertEqual(launch_fuel(11000), 2749.8)

    def test_caso_5(self):
        result = launch_fuel(6214)
        print(" Resultado:", result)
        self.assertEqual(launch_fuel(6214), 1553.4)
        
