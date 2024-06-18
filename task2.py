import random

def coin_flip():
    for i in range(100000000000000000000):
        x = int(input("Heads(1) or Tails(2)?> "))
        y = random.randint(1,2)
        if x == y:
            z = input("You were correct, would you like to play again? Yes(1) or No(2)> ")
            if z != "1":
                break
        else:
            z = input("You were incorrect, would you like to play again? Yes(1) or No(2)> ")
            if z != "1":
                break
    
        
def main():
    coin_flip()
    
if __name__ == "__main__":
    main()