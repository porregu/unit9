#Guillermo Porres, 12/9/2019
# this progrm gives two set of five random cards and compared by number and suit, then the bigger number and suit win , the wins get recorded.
import deck


def my_dealer( deck ):
    """

    :param deck: a class imported
    :return:
    """
    cards_deal = []
    for x in range(5):
        cards_deal.append(deck.deal())
    return cards_deal


def compare_cards(player1, player2):
    """

    :param player1: the cards of player one
    :param player2: the cards of player two
    :return:
    """
    if player1 > player2:
        return "player1"
    else:
        return "player2"


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    player1 = (my_dealer(my_deck))
    player2 = (my_dealer(my_deck))
    score = 0
    score2 = 0
    for x in range(5):
        print(compare_cards(player1[x], player2[x]))
        if player1[x] > player2[x]:
            score = score + 1
        else:
            score2 = score2 + 1
    print("player one was great and won ", score, "times")
    print("player two was amazing and won ", score2, "times")
    if score > score2:
        print("player one won!!! by ", score - score2)
    else:
        print("player two won !!! by ", score2 - score)


main( )