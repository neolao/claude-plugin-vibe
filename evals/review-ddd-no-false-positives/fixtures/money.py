from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    """A monetary amount in a given currency."""

    amount: int
    currency: str

    def add(self, other):
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def times(self, factor):
        return Money(self.amount * factor, self.currency)

    def exceeds(self, other):
        self._check_currency(other)
        return self.amount > other.amount

    def _check_currency(self, other):
        if other.currency != self.currency:
            raise ValueError("currency mismatch")
