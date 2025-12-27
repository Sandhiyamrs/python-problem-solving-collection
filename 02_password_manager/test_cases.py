from solution import add_password, get_password

add_password("test", "user", "pass")
assert get_password("test")["username"] == "user"
print("All tests passed")
