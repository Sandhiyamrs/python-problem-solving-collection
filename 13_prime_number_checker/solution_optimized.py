import random

class GuessGame:
    def __init__(self, low=1, high=100):
        self.number = random.randint(low, high)
        self.attempts = 0

    def make_guess(self, value):
        self.attempts += 1
        if value < self.number:
            return "Low"
        if value > self.number:
            return "High"
        return f"Correct in {self.attempts} attempts"
