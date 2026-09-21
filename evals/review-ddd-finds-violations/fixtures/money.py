class Money:
    """Represents a monetary amount in a given currency."""

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def add(self, other):
        self.amount += other.amount
        return self
