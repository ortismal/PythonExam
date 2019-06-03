class Player:
    hand = []
    def __init__(self, hand, isUser, balance, bet, playerTurn):
        self.hand = hand
        self.isUser = isUser
        self.balance = balance
        self.bet = bet
        self.playerTurn = playerTurn

    def checkSum(self):
        sum = 0
        for i in self.hand:
            if i.number == 'J' or i.number == 'Q' or i.number == 'K':
                sum += 10

            elif i.number == 'A':
                sum += 1

            else:
                sum += int(i.number)

        return sum

    def desiredBet(self):
        while(True):
            playerBet = input("Please enter your desired bet: ")
            if self.balance - int(playerBet) >= 0:
                self.bet = int(playerBet)
                break
            elif self.balance - int(playerBet) < 0:
                print("You cannot bet more than your current balance! \n Make a new bet: ")

    def checkValue(self):
        sum = self.checkSum()
        if sum == 21:
            print(f"Player has ({sum}) Dealers turn")
            self.playerTurn = False
        elif sum > 21:
            print(f"Player has lost with ({sum})")
            self.balance = self.balance - self.bet
            self.playerTurn = False
            print(f"Bet: {self.bet} \n Balance: {self.balance}")
        else:
            self.playerTurn = True

    def printCards(self):
        print("Player hand:")
        for i in self.hand:
            print(f"{i.number} of {i.suit}")
        print("Total: ", self.checkSum())
    
    def userTurn(self, dealer, deck):
        sum = self.checkSum()
        self.checkValue()
        hitOrStand = -1
        if self.isUser:
            hitOrStand = input(f"Yor current total: {sum}, would you like to hit or to stad? (type hit / stand)")
        if hitOrStand == "stand" or not self.isUser and sum > 16:
            print("Dealers turn")
            self.playerTurn = False
        elif hitOrStand == "hit" or not self.isUser and sum <= 16:
            self.hand.append(dealer.dealCards(deck))
            self.printCards()
            self.checkValue()

    def gameType(self, dealer):
        playerOrDealer = input("Play as dealer of player? (type \"p\" for player or \"d\" for dealer: ")
        
        if playerOrDealer == "p":
            dealer.isUser = False
            self.isUser = True
            print("Player is chosen")
            self.playerTurn = False

        elif playerOrDealer == "d":
            self.isUser = False
            dealer.isUser = True
            print("Dealer is chosen, game will run automaticly")
            self.playerTurn = False
            dealer.isReveal = True

        else:
            print(f"Input: {playerOrDealer} is not valid, please type \"p\" or \"d\" to continue")

    def printBalance(self):
        return print(f"Bet: {self.bet} \n Balance: {self.balance}")



