from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    """An immutable value object compared by value, not identity."""

    amount: int
    currency: str

    def add(self, other):
        if other.currency != self.currency:
            raise ValueError("currency mismatch")
        return Money(self.amount + other.amount, self.currency)
