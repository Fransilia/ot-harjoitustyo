from enum import Enum
class Suit(Enum):
    CLUB = "C"
    DIAMOND = "D"
    HEART = "H"
    SPADE = "S"

class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return self.suit.value + str(self.number)

    def __repr__(self):
        return self.suit.value + str(self.number)

    def __eq__(self,card2):
        if not isinstance(card2,Card):
            return False
        return self.number == card2.number and self.suit == card2.suit

    def card_id(self):
        return str(self.number) + self.suit.value
