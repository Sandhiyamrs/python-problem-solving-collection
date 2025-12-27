from solution_optimized import is_valid_email

assert is_valid_email("user@example.com")
assert is_valid_email("first.last@mail.co.in")
assert not is_valid_email("userexample.com")
assert not is_valid_email("user@com")
assert not is_valid_email(123)

print("All email validation tests passed")
