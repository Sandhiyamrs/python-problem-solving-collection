import random

class NumberGuessGame:
    def __init__(self, start=1, end=100):
        self.number = random.randint(start, end)
        self.attempts = 0

    def guess(self, value: int) -> str:
        self.attempts += 1
        if value < self.number:
            return "Too Low"
        if value > self.number:
            return "Too High"
        return f"Correct in {self.attempts} attempts"
