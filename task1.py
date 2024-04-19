import random

x = random.randint(1,100)

y = int(input("Please enter a number> "))

guesses = 0

while x != y :
    if y < x:
        print("That's too low")
        y = int(input("Please enter another random number> "))
    if y > x:
        print("That's too high")
        y = int(input("Please enter another random number> "))
    guesses = guesses + 1
    
    if x == y:
        print(f"Congratulations, you guessed the correct number!!! It took you {guesses} tries")
        break
    
