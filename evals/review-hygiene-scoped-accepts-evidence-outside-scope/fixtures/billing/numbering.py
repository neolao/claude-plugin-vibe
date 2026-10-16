"""Invoice numbers: one gapless sequence per year."""


class InvoiceNumberSequence:
    def __init__(self, year, last_issued=0):
        self._year = year
        self._last = last_issued

    def next(self):
        self._last += 1
        return f"{self._year}-{self._last:04d}"

    def last_issued(self):
        return self._last
