from Player import Player
from Deck import Deck
from Dealer import Dealer

player = Player([], False, 100, 0, True)
dealer = Dealer([], False, False, False, False)

gameEnd = False

while player.playerTurn:
    player.gameType(dealer)

while not gameEnd:
    deck = Deck([])
    deck.createDeck()

    player = Player([], player.isUser, player.balance, 0, True)
    dealer = Dealer([], dealer.isUser, False, False, False)

    if player.isUser:
        player.desiredBet()
        print(f"Bet: {player.bet}")
    if not player.isUser:
        player.bet = 20

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

    if player.balance == 0:
        print("Player lost, no more coin!")
        gameEnd = True
        quit()

    while True:
        replay = input("Keep playing? (y/n): ")
        if replay == "n":
            gameEnd = True
            break
        elif replay == "y":
            print("Playing again")
            break
        else:
            print("Invalid input, please type y or n")






