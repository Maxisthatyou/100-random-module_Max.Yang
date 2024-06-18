import random

x = int(input("Rock(1), paper(2), or scissors(3)?> "))
y = random.randint(1, 3)

while x == 3:
    
    if y == 2:
        print("The computer chose paper. You won!")
    elif y == 1:
        print("The computer chose scissors. Tie!")
    elif y == 3:
        print("The computer chose rock. You lost!")
    break

while x == 2:
    if y == 2:
        print("The computer chose paper. Tie!")
    elif y == 1:
        print("The computer chose scissors. You lost!")
    elif y == 3:
        print("The computer chose rock. You won!")
    break

while x == 1:
    if y == 2:
        print("The computer chose paper. You lost!")
    elif y == 1:
        print("The computer chose scissors. You won!")
    elif y == 3:
        print("The computer chose rock. Tie!")
    break
