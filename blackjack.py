import random

suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
ranks_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.val = ranks_vals[ranks.index(rank)]
        self.name = rank+suit

deck = []

for i in suits:
    for j in ranks:
        deck.append(Card(i, j))

def deal(n, deck):
    hand = []
    for _ in range(n):
        idx = random.randint(0, len(deck)-1)
        hand.append(deck.pop(idx))
    return hand

def evaluate(hand):
    val = 0
    for card in hand:
        val+=card.val
    return val

def main():
    while True:
        playerhand = deal(2, deck)
        dealerhand = deal(2, deck)

        print("Dealer's hand is: ", end="")
        print(dealerhand[0].name, ", ?")
        
        satisfied = False
        surrendered = False

        while not satisfied and not surrendered:
            print("Your hand is: ", end="")
            for card in playerhand:
                print(card.name, end=", ")
            print()

            print("What would you like to do?\nPress 1 to Hit\nPress 2 to Stand\nPress 3 to Surrender")

            choice = input("Enter your choice: ").strip()
            
            while choice not in ["1", "2", "3"]:
                choice = input("Invalid choice! Enter 1, 2 or 3: ").strip()
            
            if int(choice) == 1:
                newcard = deal(1, deck)
                playerhand.append(newcard[0])
            
            elif int(choice) == 2:
                satisfied = True

            elif int(choice) == 3:
                surrendered = True
        
        for card in playerhand:
            if card.rank == "A":
                aceval = input(f"What would you like your {card.name}'s value to be? (1/11): ")
                while aceval not in ["1", "11"]:
                    aceval = input("Please enter either 1 or 11: ")
                card.val = int(aceval)
        
        playerhand_val = evaluate(playerhand)

        dealer_play = True
        dealer_bust = False

        while dealer_play and not dealer_bust:
            print("Dealer's hand is: ", end="")
            for card in dealerhand:
                print(card.name, end=", ")
            print()

            dealerhand_val = evaluate(dealerhand)

            if dealerhand_val > 21:
                dealer_bust = True
            elif dealerhand_val > playerhand_val or dealerhand_val == 21:
                dealer_play = False
            elif dealerhand_val <= playerhand_val:
                print("Dealer hits!")
                newcard = deal(1, deck)
                dealerhand.append(newcard[0])
            
            for card in dealerhand:
                dealerhand_val = evaluate(dealerhand)
                if card.rank == "A":
                    if dealerhand_val + 11 - 1 > 21:
                        card.val = 1
                    else:
                        card.val = 11
        
        dealerhand_val = evaluate(dealerhand)

        print("Dealer's hand is worth: ", dealerhand_val)
        print("Player's hand is worth: ", playerhand_val)

        if playerhand_val>21:
            print("Player busts, dealer wins!")
        elif dealerhand_val>21:
            print("Dealer busts, player wins!")
        elif dealerhand_val>playerhand_val:
            print("Dealer wins!")
        elif playerhand_val>dealerhand_val:
            print("Player wins!")
        else:
            print("Draw!")
        
        break
main()