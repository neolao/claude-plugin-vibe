"""Memoized single-argument function."""


class Memoizer:
    def __init__(self, fn):
        self._fn = fn
        self._cache = {}

    def compute(self, x):
        if x not in self._cache:
            self._cache[x] = self._fn(x)
        return self._cache[x]
