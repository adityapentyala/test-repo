import random 

ranks = ["Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

rank_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = rank+"of"+suit
        self.val = rank_values[ranks.index(rank)]

deck = []

for rank in ranks:
    for suit in suits:
        newcard = Card(rank, suit)
        deck.append(newcard)

for card in deck:
    print(card.name, end=", ")
print()


def deal(n, deck):
    card_to_be_dealt = deck.pop(random.randint(0, len(deck)-1))
    hand = []
    hand.append(card_to_be_dealt)
    while len(hand) < n:
        card_to_be_dealt = deck.pop(random.randint(0, len(deck)-1))
        hand.append(card_to_be_dealt)
    return hand


def play():
    playerhand = deal(2, deck)
    dealerhand = deal(2, deck)

    print("Dealer's hand is: ", end="")
    print(dealerhand[0].name, "?")

    print("Your hand is: ", end="")
    for card in playerhand:
        print(card.name, end=", ")
    print()

    stood = False
    surrendered = False

    while not stood and not surrendered:
        choice = input("Enter 1 to hit, 2 to stand, 3 to surrender: ")

        if choice == "1":
            playerhand.append(deal(1, deck)[0])
            print("Your hand is: ", end="")
            for card in playerhand:
                print(card.name, end=", ")
            print()
        elif choice == "2":
            stood = True
            print("Your hand is: ", end="")
            for card in playerhand:
                print(card.name, end=", ")
            print()
        elif choice == "3":
            surrendered = True
            print("Your hand is: ", end="")
            for card in playerhand:
                print(card.name, end=", ")
            print()

    print("Player has played, it is dealer's turn")
        

    

play()