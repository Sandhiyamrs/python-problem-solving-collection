from cryptography.fernet import Fernet
from pathlib import Path

class FileEncryptor:
    def __init__(self, key: bytes):
        self.cipher = Fernet(key)

    def encrypt(self, path: str):
        file = Path(path)
        file.write_bytes(self.cipher.encrypt(file.read_bytes()))

    def decrypt(self, path: str):
        file = Path(path)
        file.write_bytes(self.cipher.decrypt(file.read_bytes()))
