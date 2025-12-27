def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False

    if "@" not in email:
        return False

    username, _, domain = email.partition("@")

    if not username or "." not in domain:
        return False

    return True


if __name__ == "__main__":
    emails = ["user@mail.com", "invalidmail", "user@site"]
    for e in emails:
        print(e, "=>", is_valid_email(e))
