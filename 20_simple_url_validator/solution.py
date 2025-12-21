import re

url = input("Enter URL: ")
pattern = re.compile(
    r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
)

if pattern.match(url):
    print("Valid URL")
else:
    print("Invalid URL")
