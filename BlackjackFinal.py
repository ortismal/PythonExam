from Player import Player
from Deck import Deck
from Dealer import Dealer

player = Player([], False, 100, 0, True)
dealer = Dealer([], False, False, False, False)
gameEnd = False

# When the game starts, player turn is automatically set to true.
while player.playerTurn:
    player.gameType(dealer)

# Game running
while not gameEnd:
    deck = Deck([])
    deck.createDeck()

    player = Player([], player.isUser, player.balance, 0, True)
    dealer = Dealer([], dealer.isUser, False, False, False)

    # Player bets
    if player.isUser:
        print(f"Your current balance is: {player.balance}")
        player.desiredBet()
        print(f"Bet: {player.bet}")
    # Player bet is fixed, if dealer gametype is chosen
    if not player.isUser:
        player.bet = 20

    # Creating the starting hands, and printing to terminal
    player.hand.append(dealer.dealCards(deck.deck))
    player.hand.append(dealer.dealCards(deck.deck))
    
    player.printCards()

    dealer.hand.append(dealer.dealCards(deck.deck))
    dealer.hand.append(dealer.dealCards(deck.deck))

    dealer.printCards()

    player.playerTurn = True

    while player.playerTurn:
        player.userTurn(dealer, deck.deck)

    dealer.dealerTurn = True
    if player.checkSum() <= 21 and not dealer.roundEnd:
        dealer.dealerTakeTurn(player, deck.deck)

    # End game if player balance hit 0
    if player.balance == 0:
        print("Player lost, no more coin!")
        gameEnd = True
        quit()

    # Decide if you want to keep playing, or end the game
    while True:
        replay = input("Keep playing? (y/n): ")
        if replay == "n":
            gameEnd = True
            break
        elif replay == "y":
            print("Playing again")
            break
        # Checks for invalid input
        else:
            print("Invalid input, please type y or n")






