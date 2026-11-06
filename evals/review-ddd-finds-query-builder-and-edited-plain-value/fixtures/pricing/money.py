class Money:
    def __init__(self, cents: int, currency: str):
        self.cents = cents
        self.currency = currency

    def plus(self, other: "Money") -> "Money":
        if other.currency != self.currency:
            raise ValueError("currency mismatch")
        return Money(self.cents + other.cents, self.currency)

    def minus(self, other: "Money") -> "Money":
        if other.currency != self.currency:
            raise ValueError("currency mismatch")
        return Money(self.cents - other.cents, self.currency)

    def times(self, factor: int) -> "Money":
        return Money(self.cents * factor, self.currency)

    def percent(self, pct: int) -> "Money":
        return Money(self.cents * pct // 100, self.currency)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Money) and (other.cents, other.currency) == (self.cents, self.currency)

    def __hash__(self) -> int:
        return hash((self.cents, self.currency))

    def __repr__(self) -> str:
        return f"Money({self.cents}, {self.currency!r})"
