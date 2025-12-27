import random

def play_game():
    number = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number (1-10): "))
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Correct!")
            break

if __name__ == "__main__":
    play_game()
