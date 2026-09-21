def validate_email_signup(data):
    if not data.get("email"):
        raise ValueError("email is required")
    if "@" not in data["email"]:
        raise ValueError("email is invalid")
    if not data.get("password"):
        raise ValueError("password is required")
    if len(data["password"]) < 8:
        raise ValueError("password is too short")
    return True


def validate_email_login(data):
    if not data.get("email"):
        raise ValueError("email is required")
    if "@" not in data["email"]:
        raise ValueError("email is invalid")
    if not data.get("password"):
        raise ValueError("password is required")
    if len(data["password"]) < 8:
        raise ValueError("password is too short")
    return True
