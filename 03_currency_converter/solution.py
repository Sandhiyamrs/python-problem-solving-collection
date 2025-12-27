RATES = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.9
}

def convert(amount, from_currency, to_currency):
    usd = amount / RATES[from_currency]
    return usd * RATES[to_currency]

if __name__ == "__main__":
    print(convert(100, "USD", "INR"))
