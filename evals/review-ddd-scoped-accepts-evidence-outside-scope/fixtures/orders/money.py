from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    cents: int
    currency: str

    def plus(self, other: "Money") -> "Money":
        if other.currency != self.currency:
            raise ValueError(f"cannot add {other.currency} to {self.currency}")
        return Money(self.cents + other.cents, self.currency)

    def times(self, factor: int) -> "Money":
        return Money(self.cents * factor, self.currency)
