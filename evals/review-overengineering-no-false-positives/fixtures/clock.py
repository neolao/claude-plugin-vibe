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


def test_frozen_clock_returns_fixed_time():
    assert FrozenClock(1_700_000_000).now() == 1_700_000_000
