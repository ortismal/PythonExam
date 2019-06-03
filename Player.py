class Player:
    hand = []
    def __init__(self, hand, isUser, balance, bet, playerTurn):
        self.hand = hand
        self.isUser = isUser
        self.balance = balance
        self.bet = bet
        self.playerTurn = playerTurn

    # Method for defining card as value
    def checkSum(self):
        currentVal = 0
        aces = 0
        for i in self.hand:
            if i.number == 'J' or i.number == 'Q' or i.number == 'K':
                currentVal += 10

            elif i.number == 'A':
                aces += 1
                for i in self.hand:
                    if i.number == 'A':
                        currentVal += self.acesValue(currentVal, aces, i)
                        aces -= 1

            # if the card is a number, cast as an int
            else:
                currentVal += int(i.number)

        return currentVal
    # Defining values of aces, as an ace can have two different values
    def acesValue(self, currentVal, aces, i):
        if i.number == 'A' and currentVal + 11 + aces - 1 > 21:
            return 1
        elif i.number == 'A':
            return 11

    # Betting method takes an input of a desired bet, check if bet is higher than balance
    def desiredBet(self):
        while(True):
            playerBet = input("Please enter your desired bet: ")
            if self.balance - int(playerBet) >= 0:
                self.bet = int(playerBet)
                break
            elif self.balance - int(playerBet) < 0:
                print("You cannot bet more than your current balance! \n Make a new bet: ")
            else:
                print("Invalid bet please type a number, and it should be less or equal to balance")

    # Check the total sum of player cards with different conditions
    def checkValue(self):
        currentVal = self.checkSum()
        if currentVal == 21:
            print(f"Player has ({currentVal}) Dealers turn")
            self.playerTurn = False
        elif currentVal > 21:
            print(f"Player has lost with ({currentVal})")
            self.balance = self.balance - self.bet
            self.playerTurn = False
            print(f"Bet: {self.bet} \n Balance: {self.balance}")
        else:
            self.playerTurn = True

    # Print the cards dealt
    def printCards(self):
        print("Player hand:")
        for i in self.hand:
            print(f"{i.number} of {i.suit}")
        print("Total: ", self.checkSum())
    
    # Choose if the player wants to hit or stay, depending on your current sum
    def userTurn(self, dealer, deck):
        currentVal = self.checkSum()
        self.checkValue()
        hitOrStand = -1
        if self.isUser:
            hitOrStand = input(f"Yor current total: {currentVal}, would you like to hit or to stad? (type hit / stand)")
        if hitOrStand == "stand" or not self.isUser and currentVal > 16:
            print("Dealers turn")
            self.playerTurn = False
        elif hitOrStand == "hit" or not self.isUser and currentVal <= 16:
            self.hand.append(dealer.dealCards(deck))
            self.printCards()
            self.checkValue()

    # Choose to play as the dealer or a player
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



