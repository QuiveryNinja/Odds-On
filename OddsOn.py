import random

print("The following is a program where you can place your odds on!")
print("Write down the range of your guess: ")
print("from: 1")
toNum = int(input("to: "))

guess = int(input("guess: "))

def Generate():
    randomNum = random.randrange(1, toNum)
    if guess == randomNum:
        print("Congrats! You won!")
        print("the generated number was", randomNum)
        print("your number was", guess)
    else:
        print("You lost...")
        print("the generated number was", randomNum)
        print("your number was", guess)

Generate()