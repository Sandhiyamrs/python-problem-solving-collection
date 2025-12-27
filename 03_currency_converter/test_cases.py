from solution import convert

assert round(convert(100, "USD", "INR")) == 8300
assert round(convert(83, "INR", "USD")) == 1
print("Currency tests passed")
