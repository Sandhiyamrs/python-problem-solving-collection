from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(path, key):
    cipher = Fernet(key)
    with open(path, "rb") as f:
        encrypted = cipher.encrypt(f.read())
    with open(path, "wb") as f:
        f.write(encrypted)
