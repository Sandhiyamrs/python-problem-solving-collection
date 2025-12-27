import json

DATA_FILE = "passwords.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def add_password(service, username, password):
    data = load_data()
    data[service] = {"username": username, "password": password}
    save_data(data)

def get_password(service):
    data = load_data()
    return data.get(service, "Service not found")

if __name__ == "__main__":
    add_password("gmail", "user@gmail.com", "1234")
    print(get_password("gmail"))
