class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return self.suit + str(self.number)

    def __repr__(self):
        return self.suit + str(self.number)
