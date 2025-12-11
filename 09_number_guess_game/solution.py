import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess (1-100): "))

    if guess == num:
        print("Correct! 🎉")
        break
    elif guess < num:
        print("Too Low!")
    else:
        print("Too High!")
