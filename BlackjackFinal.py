from Player import Player
from Deck import Deck
from Dealer import Dealer

player = Player([], False, 100, 0, True)
dealer = Dealer([], False, False, False, False)

# a boolean that defines if the game is over or not
gameEnd = False

while player.playerTurn:
    player.gameType(dealer)

# The game is running while gameEnd is false
while not gameEnd:
    deck = Deck([])
    deck.createDeck()

    player = Player([], player.isUser, player.balance, 0, True)
    dealer = Dealer([], dealer.isUser, False, False, False)

    # Player bets
    if player.isUser:
        player.desiredBet()
        print(f"Bet: {player.bet}")
    
    # Player bet is fixed, if the user is playing as the dealer.
    if not player.isUser:
        player.bet = 20

    # Creates starting hands, and printing to terminal
    player.hand.append(dealer.dealCards(deck.deck))
    player.hand.append(dealer.dealCards(deck.deck))
    
    player.printCards()

    dealer.hand.append(dealer.dealCards(deck.deck))
    dealer.hand.append(dealer.dealCards(deck.deck))

    dealer.printCards()

    player.playerTurn = True
    # TODO player.isBlackjack
    while player.playerTurn:
        player.userTurn(dealer, deck.deck)

    dealer.dealerTurn = True
    if player.checkSum() <= 21 and not dealer.roundEnd:
        dealer.dealerTakeTurn(player, deck.deck)

    # Game ends if the player balance is 0.
    if player.balance == 0:
        print("Player balance is empty. Game over!")
        gameEnd = True
        quit()

    # Decide whether to keep playing, or end game
    while True:
        replay = input("Keep playing? (y/n): ")
        if replay == "n":
            gameEnd = True
            break
        elif replay == "y":
            print("Playing again")
            break
        # Check for invalid inputs
        else:
            print("Invalid input, please type y or n")






