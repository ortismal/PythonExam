from Deck import Deck

class Dealer:
    hand = []

    def __init__(self, hand, isUser, isReveal, dealerTurn, roundEnd):
        self.hand = hand
        self.isUser = isUser
        self.isReveal = isReveal
        self.dealerTurn = dealerTurn
        self.roundEnd = roundEnd

    # Deal card and remove from the "deck"
    def dealCards(self, deck):
        return deck.pop()
    
    # Method for defining card as value
    def checkSum(self):
        aces = 0
        currentDealerValue = 0
        for i in self.hand:
            if i.number == 'J' or i.number== 'Q' or i.number == 'K':
                currentDealerValue += 10

            elif i.number == 'A':
                aces += 1
                for i in self.hand:
                    if i.number == 'A':
                        currentDealerValue += self.acesValue(currentDealerValue, aces, i)
                        aces -= 1
            else:
                currentDealerValue += int(i.number)

        return currentDealerValue

    # Method for defining value of aces (used in above method), to act as ace can have 2 values
    def acesValue(self, currentDealerValue, aces, i):
        if i.number == 'A' and currentDealerValue + 11 + aces - 1 > 21:
            return 1
        elif i.number == 'A':
            return 11

    # Make the dealer take his/hers turn, and run method to check winning hand compared to player
    def dealerTakeTurn(self, player, deck):
        self.isReveal = True
        self.printCards()
        self.checkWin(player)
        self.dealerTurn = True
        # Dealer have to "hit" if the total is less than 16, and stand if 17 or above
        while self.dealerTurn:
            currentDealerValue = self.checkSum()
            if currentDealerValue <= 16:
                print("Dealer has less than 16, so force-hit")
                self.hand.append(self.dealCards(deck))
                self.printCards()
                self.checkWin(player)
            else:
                self.dealerTurn = False

    # Print a visual of the cards dealt
    def printCards(self):
        # When comparing hands, dealer must "show" both cards
        if self.isReveal:
            for i in self.hand:
                print(f"{i.number} of {i.suit}")
            print("Total: ", self.checkSum())
        # When dealer has been given cards (2), and it is players turn, dealer has 1 hidden card
        if not self.isReveal:
            print("Dealer hand:")
            print(f"{self.hand[1].number} of {self.hand[1].suit}")
            print("1 hidden card")

    # Dealer method for the comparing of hands, and defining the outcome based on different conditions
    def checkWin(self, player):
        currentPlayerValue = player.checkSum()
        currentDealerValue = self.checkSum()
        if currentDealerValue > 21:
            print("Dealer is bust (more than 21)")
            player.balance += player.bet * 2
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True
        
        elif currentDealerValue > currentPlayerValue and currentDealerValue > 16:
            print(f"Dealer has: {currentDealerValue}, and wins. \n Player has: {currentPlayerValue}")
            player.balance = player.balance - player.bet
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        elif currentDealerValue == currentPlayerValue and currentDealerValue > 16:
            print(f"Tied game, both has: {currentDealerValue}")
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        elif currentDealerValue < currentPlayerValue and currentDealerValue > 16:
            print(f"Dealer lost with: {currentDealerValue}. Player got: {currentPlayerValue}")
            player.balance += player.bet * 2
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        else:
            self.dealerTurn = True
