import unittest
from freecodecamp.src.battle_of_words import battle

class TestBattleOfWords(unittest.TestCase):
    def test_hello(self):
        result = battle("hello world", "hello word")
        print("Resultado:", result)
        self.assertEqual(result, "We win")

    def test_kitty(self):
        result = battle("lorem ipsum", "kitty ipsum")
        print("Resultado:", result)
        self.assertEqual(result, "We lose")

    def test_world(self):
        result = battle("hello world", "world hello")
        print("Resultado:", result)
        self.assertEqual(result, "Draw")

    def test_switch(self):
        result = battle("git checkout", "git switch")
        print("Resultado:", result)
        self.assertEqual(result, "We win")

    def surrender(self):
        result = battle("We must never surrender", "Our team must win")
        print("Resultado:", result)
        self.assertEqual(result, "Draw")

