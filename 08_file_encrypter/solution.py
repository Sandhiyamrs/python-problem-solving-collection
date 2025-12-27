from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, "rb") as f:
        data = f.read()

    encrypted_data = cipher.encrypt(data)

    with open(filename, "wb") as f:
        f.write(encrypted_data)

def decrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(filename, "wb") as f:
        f.write(decrypted_data)
