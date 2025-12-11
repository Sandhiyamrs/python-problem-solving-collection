import random
import string

def generate_password(length=14):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

site = input("Enter website/app name: ")
password = generate_password()

with open("passwords.txt", "a") as f:
    f.write(f"{site}: {password}\n")

print("Generated Password:", password)
print("Saved to passwords.txt")
