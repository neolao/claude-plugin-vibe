from abc import ABC, abstractmethod


class Clock(ABC):
    """Time seam: production uses SystemClock; tests substitute FrozenClock
    below to assert on fixed timestamps instead of real wall-clock time."""

    @abstractmethod
    def now(self):
        raise NotImplementedError


class SystemClock(Clock):
    def now(self):
        import time

        return time.time()


class FrozenClock(Clock):
    def __init__(self, fixed_time):
        self._fixed_time = fixed_time

    def now(self):
        return self._fixed_time


class SessionExpiry:
    """Called by the auth middleware on every request."""

    def __init__(self, clock, ttl_seconds):
        self._clock = clock
        self._ttl_seconds = ttl_seconds

    def is_expired(self, started_at):
        return self._clock.now() - started_at > self._ttl_seconds


def build_session_expiry():
    return SessionExpiry(SystemClock(), ttl_seconds=1800)


def test_session_expires_after_ttl():
    expiry = SessionExpiry(FrozenClock(10_000), ttl_seconds=1800)
    assert expiry.is_expired(started_at=8_000)
    assert not expiry.is_expired(started_at=9_000)
