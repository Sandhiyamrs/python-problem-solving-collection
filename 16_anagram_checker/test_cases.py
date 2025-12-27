from solution_optimized import FileEncryptor
from cryptography.fernet import Fernet

key = Fernet.generate_key()
encryptor = FileEncryptor(key)

with open("secret.txt", "w") as f:
    f.write("Top Secret")

encryptor.encrypt("secret.txt")
encryptor.decrypt("secret.txt")

assert open("secret.txt").read() == "Top Secret"
print("File Encryptor tests passed")
