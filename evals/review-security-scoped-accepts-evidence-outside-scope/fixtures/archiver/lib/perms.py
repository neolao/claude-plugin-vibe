ALLOWED = {
    "pack": {"operator", "admin"},
    "restore": {"admin"},
    "share": {"operator", "admin"},
    "rotate_key": {"admin"},
}


class Forbidden(Exception):
    pass


def require(user, action):
    roles = ALLOWED.get(action)
    if roles is None or user.role not in roles:
        raise Forbidden(f"{user.name} may not {action}")
