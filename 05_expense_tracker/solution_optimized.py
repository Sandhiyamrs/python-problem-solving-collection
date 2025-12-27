from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self._expenses = defaultdict(float)

    def add_expense(self, category: str, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._expenses[category] += amount

    def total_expense(self) -> float:
        return sum(self._expenses.values())

    def summary(self) -> dict:
        return dict(self._expenses)
