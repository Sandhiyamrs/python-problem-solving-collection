expenses = []

while True:
    item = input("Item (q to quit): ")
    if item == 'q':
        break

    amt = float(input("Amount: "))
    expenses.append((item, amt))

print("\n--- Expense Summary ---")
for item, amt in expenses:
    print(f"{item}: ₹{amt}")

print("Total Spent: ₹", sum(x[1] for x in expenses))
