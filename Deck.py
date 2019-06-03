import random
from Cards import Cards

class Deck:
    deck = []
    def __init__(self, deck):
        self.deck = deck

    # Create deck with suits and values
    def createDeck(self):
        deckValues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deckSuits = ['♥', '♠', '♦', '♣']

        # Make 52 unique cards
        for suit in deckSuits:
            for number in deckValues:
                self.deck.append(Cards(suit, number))

        # Shuffle deck
        random.shuffle(self.deck)
        return self.deck