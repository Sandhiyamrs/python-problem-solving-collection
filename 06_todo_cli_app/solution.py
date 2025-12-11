tasks = []

while True:
    print("\n1) Add Task  2) View Tasks  3) Exit")
    ch = input("Choose: ")

    if ch == "1":
        tasks.append(input("Task: "))
    elif ch == "2":
        print("\nTasks:")
        for t in tasks:
            print("-", t)
    elif ch == "3":
        break
