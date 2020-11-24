import unittest
from entities.card import Card, Suit
from entities.gamestate import GameState 

class TestGameState(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_deckofcards_created(self):
        self.assertEqual(len(GameState.fulldeck(self)),52)

    def test_gamestate_right_amount_cards(self):
        state = GameState(14)
        self.assertEqual(len(state.deck),14)
        state = GameState(64)
        self.assertEqual(len(state.deck),64)

    def test_gamestate_add_answer(self):
        state = GameState(2)
        card = Card(2,Suit.DIAMOND)
        state.add_answer(card)
        self.assertEqual(len(state.get_answers()),1)
        self.assertEqual(state.get_answers()[0],card)
        card2 = Card(3,Suit.CLUB)
        state.add_answer(card2)
        self.assertEqual(len(state.get_answers()),2)
        self.assertEqual(state.get_answers()[1],card2)

    def test_gamestate_all_answers_done(self):
        state = GameState(2)
        card = Card(2,Suit.DIAMOND)
        state.add_answer(card)
        self.assertFalse(state.all_answers_done())
        card2 = Card(3,Suit.CLUB)
        state.add_answer(card2)
        self.assertTrue(state.all_answers_done())
