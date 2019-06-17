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
        currentPlayerVal = 0
        aces = 0
        for i in self.hand:
            if i.number == 'J' or i.number == 'Q' or i.number == 'K':
                currentPlayerVal += 10

            elif i.number == 'A':
                aces += 1
                for i in self.hand:
                    if i.number == 'A':
                        currentPlayerVal += self.acesValue(currentPlayerVal, aces, i)
                        aces -= 1

            # if just a numbered card cast as int and add to value
            else:
                currentPlayerVal += int(i.number)

        return currentPlayerVal

    # Method for defining value of aces (used in above method), to act as ace can have 2 values
    def acesValue(self, currentPlayerVal, aces, i):
        if i.number == 'A' and currentPlayerVal + 11 + aces - 1 > 21:
            return 1
        elif i.number == 'A':
            return 11

    # Betting method to make input of desired bet, checkup on bet is higher than balance
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

    # Ceck the total sum of player cards /w different conditions
    def checkValue(self):
        currentPlayerVal = self.checkSum()
        if currentPlayerVal == 21:
            print(f"Player has ({currentPlayerVal}) Dealers turn")
            self.playerTurn = False
        elif currentPlayerVal > 21:
            print(f"Player has lost with ({currentPlayerVal})")
            self.balance = self.balance - self.bet
            self.playerTurn = False
            print(f"Bet: {self.bet} \n Balance: {self.balance}")
        else:
            # Still player turn
            self.playerTurn = True

    # Print a visual of the cards dealt
    def printCards(self):
        print("Player hand:")
        for i in self.hand:
            print(f"{i.number} of {i.suit}")
        print("Total: ", self.checkSum())
    # Choose if as player you want to stay/hit depending on your current total
    def userTurn(self, dealer, deck):
        currentPlayerVal = self.checkSum()
        self.checkValue()
        hitOrStand = -1
        if self.isUser:
            hitOrStand = input(f"Yor current total: {currentPlayerVal}, would you like to hit or to stad? (type hit / stand)")
        if hitOrStand == "stand" or not self.isUser and currentPlayerVal > 16:
            print("Dealers turn")
            self.playerTurn = False
        elif hitOrStand == "hit" or not self.isUser and currentPlayerVal <= 16:
            self.hand.append(dealer.dealCards(deck))
            self.printCards()
            self.checkValue()

    # As user pick a gametype (play as dealer or player)
    def gameType(self, dealer):
        playerOrDealer = input("Play as dealer of player? (type \"p\" for player or \"d\" for dealer: ")
        
        if playerOrDealer == "p":
            dealer.isUser = False
            self.isUser = True
            print("Player is chosen")
            self.playerTurn = False

        elif playerOrDealer == "d":
            dealer.isUser = True
            self.isUser = False
            print("Dealer is chosen, game will run automaticly")
            self.playerTurn = False
            dealer.isReveal = True

        # Only accept valid input
        else:
            print(f"Input: {playerOrDealer} is not valid, please type \"p\" or \"d\" to continue")
    
    def printBalance(self):
        return print(f"Bet: {self.bet} \n Balance: {self.balance}")



