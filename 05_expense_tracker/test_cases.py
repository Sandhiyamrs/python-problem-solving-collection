from solution_optimized import ExpenseTracker

tracker = ExpenseTracker()
tracker.add_expense("Food", 300)
tracker.add_expense("Food", 200)
tracker.add_expense("Travel", 150)

assert tracker.total_expense() == 650
assert tracker.summary()["Food"] == 500

print("Expense tracker tests passed")
