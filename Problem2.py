import random
card = []
suits = ["of Spade", "of Diamond", "of Heart", "of Club"]
def card():
    for i in range(10000000):
        for i in range(4):
            card.append("Ace")
        for i in range(2, 10):
            card.append(i)
            card.append(i)
            card.append(i)
            card.append(i)
        for i in range(4):
            card.append("Jack")
            card.append("King")
            card.append("Queen")
        for i in range(2):
            for j in range(5):
                randomCard = random.randint(0, len(card) - 1)
                randomSuit = random.randint(0, 3)
                print(card[randomCard], suits[randomSuit])
                card.pop(randomCard)
            print()
        for i in range(10000000):
            x = input("Would you like to draw another 5? (1.Yes)(2.No)")
            if x == "2":
                print("Thank you for playing")
                break
            elif x == "1":
                print("Ok, here's another hand")
            
            else:
                print("Invalid input")
        