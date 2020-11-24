from entities.card import Card, Suit
import math
import random

class GameState:
    def __init__(self, amount):
        self.deck = self.random_deck_of_size(amount)
        self.answers =[]

    def fulldeck(self):
        deck =[]
        for suit in [Suit.CLUB, Suit.DIAMOND, Suit.HEART, Suit.SPADE]:
            for i in range(1,14):
                deck.append(Card(i, suit))
        return deck

    def random_fulldeck(self):
        deck = self.fulldeck()
        random.shuffle(deck)
        return deck

    def random_deck_of_size(self, amount):
        deck = []
        deck_ammount = math.ceil(amount/52)
        for i in range(0,deck_ammount):
            deck.extend(self.random_fulldeck())
        cards_to_remove = deck_ammount*52 - amount
        return deck[cards_to_remove:]

    def add_answer(self, card):
        self.answers.append(card)

    def get_answers(self):
        return self.answers

    def all_answers_done(self):
        return len(self.deck) <= len(self.answers)

    def print_status(self):
        print(self.deck)
    