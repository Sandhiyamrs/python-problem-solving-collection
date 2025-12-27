from decimal import Decimal

RATES = {
    "USD": Decimal("1.0"),
    "INR": Decimal("83.0"),
    "EUR": Decimal("0.9")
}

def convert(amount, src, dest):
    amount = Decimal(str(amount))
    return (amount / RATES[src]) * RATES[dest]
