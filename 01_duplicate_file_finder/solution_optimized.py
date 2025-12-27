import os
import hashlib

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            file_hash = hash_file(path)
            if file_hash in hashes:
                duplicates.append(file)
            else:
                hashes[file_hash] = file

    return duplicates

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    print(find_duplicates(folder))
