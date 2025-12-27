from solution_optimized import SecureFile
from cryptography.fernet import Fernet

key = Fernet.generate_key()
secure = SecureFile(key)

with open("sample.txt", "w") as f:
    f.write("Hello Secure World")

secure.encrypt("sample.txt")
secure.decrypt("sample.txt")

assert open("sample.txt").read() == "Hello Secure World"
print("File encrypter tests passed")
