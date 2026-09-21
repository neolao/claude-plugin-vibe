def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


class Memoizer:
    def __init__(self):
        self._cache = {}

    def compute(self, n):
        if n not in self._cache:
            self._cache[n] = n * n
        return self._cache[n]
