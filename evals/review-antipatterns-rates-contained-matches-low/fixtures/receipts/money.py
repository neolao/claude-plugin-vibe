from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    cents: int
    currency: str

    def plus(self, other):
        if other.currency != self.currency:
            raise ValueError("currency mismatch")
        return Money(self.cents + other.cents, self.currency)
