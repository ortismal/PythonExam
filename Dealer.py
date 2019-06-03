from Deck import Deck

class Dealer:
    hand = []
    def __init__(self, hand, isUser, isReveal, dealerTurn, roundEnd):
        self.hand = hand
        self.isUser = isUser
        self.isReveal = isReveal
        self.dealerTurn = dealerTurn
        self.roundEnd = roundEnd

    # Deal a card and remove it from the deck
    def dealCards(self, deck):
        return deck.pop()
    
    # Method for defining card value
    def checkSum(self):
        aces = 0
        currentVal = 0
        for i in self.hand:
            if i.number == 'J' or i.number== 'Q' or i.number == 'K':
                currentVal += 10

            elif i.number == 'A':
                aces += 1
                for i in self.hand:
                    if i.number == 'A':
                        currentVal += self.acesValue(currentVal, aces, i)
                        aces -= 1
            else:
                currentVal += int(i.number)

            

        return currentVal

    # Defining value of aces
    def acesValue(self, currentVal, aces, i):
        if i.number == 'A' and currentVal + 11 + aces - 1 > 21:
            return 1
        elif i.number == 'A':
            return 11

    # Makes dealer take his/her turn, and run method to check winning hand compared to player
    def dealerTakeTurn(self, player, deck):
        self.isReveal = True
        self.printCards()
        self.checkWin(player)
        self.dealerTurn = True
        # Dealer have to "hit" if the total is less than 16, and stand if the sum is 17 or above
        while self.dealerTurn:
            currentVal = self.checkSum()
            if currentVal <= 16:
                print("Dealer has less than 16, so force-hit")
                self.hand.append(self.dealCards(deck))
                self.printCards()
                self.checkWin(player)
            else:
                self.dealerTurn = False

    # Print the cards dealt
    def printCards(self):
        # When comparing hands, dealer must show both cards
        if self.isReveal:
            for i in self.hand:
                print(f"{i.number} of {i.suit}")
            print("Total: ", self.checkSum())
        # When dealer is dealt 2 cards, and the player has the turn, the second dealer card is hidden.
        if not self.isReveal:
            print("Dealer hand:")
            print(f"{self.hand[1].number} of {self.hand[1].suit}")
            print("1 hidden card")

    # Method for comparing hands, and defining outcome based on different conditions
    def checkWin(self, player):
        playerSum = player.checkSum()
        currentVal = self.checkSum()
        if currentVal > 21:
            print("Dealer is bust (more than 21)")
            player.balance += player.bet * 2
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True
        
        elif currentVal > playerSum and currentVal > 16:
            print(f"Dealer has: {currentVal}, and wins. \n Player has: {playerSum}")
            player.balance = player.balance - player.bet
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        elif currentVal == playerSum and currentVal > 16:
            print(f"Tied game, both has: {currentVal}")
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        elif currentVal < playerSum and currentVal > 16:
            print(f"Dealer lost with: {currentVal}. Player got: {playerSum}")
            player.balance += player.bet * 2
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        else:
            self.dealerTurn = True
