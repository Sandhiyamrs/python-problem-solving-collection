from solution_optimized import FileEncrypter
from cryptography.fernet import Fernet

key = Fernet.generate_key()
encrypter = FileEncrypter(key)

with open("test.txt", "w") as f:
    f.write("Secret Data")

encrypter.encrypt("test.txt")
encrypter.decrypt("test.txt")

with open("test.txt") as f:
    assert f.read() == "Secret Data"

print("File encryption tests passed")
