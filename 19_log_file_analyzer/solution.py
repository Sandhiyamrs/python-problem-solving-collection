file_path = input("Enter log file path: ")

errors = 0
warnings = 0

with open(file_path, "r") as file:
    for line in file:
        if "ERROR" in line:
            errors += 1
        elif "WARNING" in line:
            warnings += 1

print("Errors:", errors)
print("Warnings:", warnings)
