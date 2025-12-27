import random

def play():
    number = random.randint(1, 20)
    while True:
        guess = int(input("Guess the number: "))
        if guess == number:
            print("Correct!")
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")
