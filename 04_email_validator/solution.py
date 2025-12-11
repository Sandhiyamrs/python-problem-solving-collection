import re

email = input("Enter Email: ")

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(pattern, email):
    print("Valid Email ✔")
else:
    print("Invalid Email ❌")
