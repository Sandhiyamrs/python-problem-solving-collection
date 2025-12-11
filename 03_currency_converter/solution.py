import requests

def convert(amount, from_c, to_c):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_c}"
    data = requests.get(url).json()
    rate = data["rates"][to_c]
    return amount * rate

amt = float(input("Amount: "))
from_currency = input("From currency (USD): ").upper()
to_currency = input("To currency (INR): ").upper()

result = convert(amt, from_currency, to_currency)
print("Converted Amount:", round(result, 2))
