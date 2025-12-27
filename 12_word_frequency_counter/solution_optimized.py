from cryptography.fernet import Fernet
from pathlib import Path

class SecureFile:
    def __init__(self, key: bytes):
        self.cipher = Fernet(key)

    def encrypt(self, file_path: str):
        file = Path(file_path)
        file.write_bytes(self.cipher.encrypt(file.read_bytes()))

    def decrypt(self, file_path: str):
        file = Path(file_path)
        file.write_bytes(self.cipher.decrypt(file.read_bytes()))
