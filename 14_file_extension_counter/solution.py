import os

folder = input("Enter folder path: ")
extensions = {}

for file in os.listdir(folder):
    if "." in file:
        ext = file.split(".")[-1]
        extensions[ext] = extensions.get(ext, 0) + 1

for ext, count in extensions.items():
    print(ext, ":", count)
