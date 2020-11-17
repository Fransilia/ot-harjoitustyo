import unittest
from entities.gamestate import GameState 

class TestGameState(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_tavallinen_pakka_muodostuu_oikein(self):
        self.assertEqual(len(GameState.fulldeck(self)),52)
