"""Login sessions. `created_at` is stored in UTC by the login handler (sessions/login.py)."""
from datetime import datetime, timedelta, timezone

SESSION_TTL = timedelta(hours=12)


def new_session(user_id):
    return {"user": user_id, "created_at": datetime.now(timezone.utc)}


def is_expired(session):
    return datetime.now() - session["created_at"] > SESSION_TTL
