from . import ids


def share_token():
    return ids.short_id(24)


def api_key():
    return ids.secure_id(32)
