import json
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
cipher = Fernet(KEY)
FILE = "secure_passwords.json"

def load():
    try:
        with open(FILE, "rb") as f:
            return json.loads(cipher.decrypt(f.read()))
    except:
        return {}

def save(data):
    with open(FILE, "wb") as f:
        f.write(cipher.encrypt(json.dumps(data).encode()))

def add(service, username, password):
    data = load()
    data[service] = {"username": username, "password": password}
    save(data)

def fetch(service):
    return load().get(service, "Not found")
