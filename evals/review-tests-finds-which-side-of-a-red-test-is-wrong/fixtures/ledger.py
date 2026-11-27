"""Running balance of one account."""


class Ledger:
    def __init__(self):
        self._entries = []

    def post(self, amount, memo):
        """Record one entry; a refund is a negative amount."""
        self._entries.append((amount, memo))

    def balance(self):
        return sum(amount for amount, _ in self._entries)

    def memos(self):
        return [memo for _, memo in self._entries]
