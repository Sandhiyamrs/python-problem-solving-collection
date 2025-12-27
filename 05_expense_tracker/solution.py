expenses = []

def add_expense(amount: float, category: str):
    expenses.append({"amount": amount, "category": category})

def total_expense() -> float:
    return sum(item["amount"] for item in expenses)

def category_summary():
    summary = {}
    for item in expenses:
        summary[item["category"]] = summary.get(item["category"], 0) + item["amount"]
    return summary


if __name__ == "__main__":
    add_expense(250, "Food")
    add_expense(120, "Travel")
    add_expense(80, "Food")
    print("Total:", total_expense())
    print("Summary:", category_summary())
