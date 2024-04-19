import random
x = int(input("Heads(1) or tails(2)?> "))
y = random.randint(1, 2)

while x == y:
    print(f"You guessed it!",end = ' ')
    z = input("Would you like to play again> ")
    y = random.randint(1, 2)
    if z != "yes":
        break
    x = int(input("Heads(1) or tails(2)?> "))
while x != y:
    print("Sorry, you were incorrect!",end = " ")
    z = input("Would you like to play again> ")
    y = random.randint(1, 2)
    if z != "yes":
        break
    x = int(input("Heads(1) or tails(2)?> "))
    