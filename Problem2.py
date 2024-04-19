import random
card = []
suits = ["of Spade", "of Diamond", "of Heart", "of Club"]
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