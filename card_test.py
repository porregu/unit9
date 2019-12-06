import card
import deck


def my_dealer(deck):
    cards_deal = []
    for x in range(5):
        cards_deal.append(deck.deal())
    return cards_deal

def compare_cards(player1, player2):
    if player1 > player2:
        return "player1"
    else:
        return "player2"

def main ():
    my_deck = deck.Deck()
    my_deck.shuffle()
    player1 = (my_dealer(my_deck))
    player2 = (my_dealer(my_deck))
    score = []
    #score2 = []
    for x in range(5):
        print(compare_cards(player1[x], player2[x]))
    if player1[x] > player2[x]:
        score = score + 1
    else:
        score = score + 2
    print(score)

main()