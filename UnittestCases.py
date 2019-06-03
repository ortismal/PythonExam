import unittest
from Player import Player
from Deck import Deck
from Dealer import Dealer
from Cards import Cards



class uTestDeck(unittest.TestCase):
    
    # Test 1.1 deck size
    def test_deck_size(self):
        test_deck = Deck.createDeck(Deck)
        self.assertEqual(len(test_deck), 52, "Deck size should = 52")
    # Test 1.2 deck size after dealt card
    def test_pop_size(self):
        deck = Deck.deck
        Dealer.dealCards(Deck, deck)
        self.assertEqual(len(deck), 51, "Deck size should = 51 (card drawn)")
    
class uTestHand(unittest.TestCase):

    # Test 2.1 Hand size after dealt cards
    def test_hand_size_start(self):
        player = Player([], False, 100, 0, True)
        dealer = Dealer([], False, False, False, False)
        # Dealing cards:
        player.hand.append(dealer.dealCards(Deck.deck))
        player.hand.append(dealer.dealCards(Deck.deck))
        dealer.hand.append(dealer.dealCards(Deck.deck))
        dealer.hand.append(dealer.dealCards(Deck.deck))
        self.assertEqual(len(player.hand), 2, "Player hand size should be 2"), 
        self.assertEqual(len(dealer.hand), 2, "Dealer hand size should be 2")

    # Test 2.2 Hand size greater for player on "hit"
    def test_hand_size_greater(self):
        # 2 cards has been added
        player = Player([0, 1], False, 100, 0, True)
        dealer = Dealer([], False, False, False, False)
        
        hitOrStand = "hit"
        if hitOrStand == "hit":
            player.hand.append(dealer.dealCards(Deck.deck))
            self.assertEqual(len(player.hand), 3, "Player hand size should be 3")

    
class uTestHandSum(unittest.TestCase):
    # Test 3.1 Test for correct outcome of cards
    def test_sum_hand(self):
        player = Player([Cards("♥", "K"), Cards("♠", "10")], False, 100, 0, True)
        dealer = Dealer([Cards("♦", "7"), Cards("♣", "10")], False, False, False, False)

        self.assertEqual(player.checkSum(), 20, "Player hand should be = 20"),
        self.assertEqual(dealer.checkSum(), 17, "Dealer hand should be = 17"),


if __name__ == '__main__':
    unittest.main()