"""Login handler: opens a session after the password check."""
from sessions.store import new_session, is_expired

SESSIONS = {}


def login(user_id, password_ok):
    if not password_ok:
        return None
    SESSIONS[user_id] = new_session(user_id)
    return SESSIONS[user_id]


def current_user(user_id):
    session = SESSIONS.get(user_id)
    if session is None or is_expired(session):
        return None
    return session["user"]
