"""Sessions currently signed in, by token."""

SESSION_CACHE = {}


def user_for(token):
    return SESSION_CACHE.get(token)
