from Deck import Deck

class Dealer:
    hand = []
    def __init__(self, hand, isUser, isReveal, dealerTurn, roundEnd):
        self.hand = hand
        self.isUser = isUser
        self.isReveal = isReveal
        self.dealerTurn = dealerTurn
        self.roundEnd = roundEnd

    def dealCards(self, deck):
        return deck.pop()
    
    def checkSum(self):
        aces = 0
        sum = 0
        for i in self.hand:
            if i.number == 'J' or i.number== 'Q' or i.number == 'K':
                sum += 10

            elif i.number == 'A':
                aces += 1

            else:
                sum += int(i.number)

            for i in self.hand:
                if i.number == 'A':
                    if self.acesValue(sum, aces):
                        sum += 1
                    else:
                        sum += 11
                    aces -= 1

        return sum

    def acesValue(self, sum, aces):
        if sum + 11 + aces - 1 > 21:
            return True
        else:
            return False

    def dealerTakeTurn(self, player, deck):
        self.isReveal = True
        self.printCards()
        self.checkWin(player)
        self.dealerTurn = True
        while self.dealerTurn:
            sum = self.checkSum()
            if sum <= 16:
                print("Dealer has less than 16, so force-hit")
                self.hand.append(self.dealCards(deck))
                self.printCards()
                self.checkWin(player)
            else:
                self.dealerTurn = False

    def printCards(self):
        if self.isReveal:
            for i in self.hand:
                print(f"{i.number} of {i.suit}")
            print("Total: ", self.checkSum())
        if not self.isReveal:
            print("Dealer hand:")
            print(f"{self.hand[1].number} of {self.hand[1].suit}")
            print("1 hidden card")

    def checkWin(self, player):
        playerSum = player.checkSum()
        sum = self.checkSum()
        if sum > 21:
            print("Dealer is bust (more than 21)")
            player.balance += player.bet * 2
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True
        
        elif sum > playerSum and sum > 16:
            print(f"Dealer has: {sum}, and wins. \n Player has: {playerSum}")
            player.balance = player.balance - player.bet
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        elif sum == playerSum and sum > 16:
            print(f"Tied game, both has: {sum}")
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        elif sum < playerSum and sum > 16:
            print(f"Dealer lost with: {sum}. Player got: {playerSum}")
            player.balance += player.bet * 2
            player.printBalance()
            self.dealerTurn = False
            self.roundEnd = True

        else:
            self.dealerTurn = True
