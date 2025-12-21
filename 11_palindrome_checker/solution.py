text = input("Enter a string: ").lower().replace(" ", "")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
