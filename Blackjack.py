import random

#Cards:
d_cards = []
p_cards = []

#Deal:
while len(d_cards) != 2:
    d_cards.append(random.randint(1, 11))
    if len(d_cards) == 2:
        print("Dealer got hidden card + " , d_cards[1])

while len(p_cards) != 2:
    p_cards.append(random.randint(1, 11))
    if len(p_cards) == 2:
        print("You have " , p_cards , "Your total: " + str(sum(p_cards)))



while sum(p_cards) < 22:
    action = str(input("stay/hit? "))
    if action == "hit":
        p_cards.append(random.randint(1, 11))
        print("Your actual total: " + str(sum(p_cards)) + ", cards: " , p_cards)
    else:
        if sum(d_cards) == 21:
            print("Dealer win with \"Blackjack\"")
            break
        while sum(d_cards) < 17:
            d_cards.append(random.randint(1, 11))
            #print(sum(d_cards))
            if (len(d_cards) == 5 & sum(d_cards) == 21):
                print("Dealer win with \"Blackjack\"")
                break
        if sum(d_cards) > 21:
            print("Dealer lost, has more than 21, dealer has: " + str(sum(d_cards)))
            break
        print("Dealer total: " + str(sum(d_cards)) + ", cards: " , d_cards)
        print("Your total: " + str(sum(p_cards)) + ", cards: " , p_cards)
        if sum(d_cards) >= sum(p_cards):
            print("Dealer won")
            break
        if sum(p_cards) == 21:
            print("You have \"Blackjack\", you won")
            break
        else:
            print("You won")
            break
        

if sum(p_cards) > 21:
    print("You lost, more than 21")
        

