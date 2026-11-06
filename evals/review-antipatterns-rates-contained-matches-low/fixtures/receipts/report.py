"""Daily receipts report. Built by the end-of-day job."""


class Report:
    def __init__(self, store):
        self._store = store
        self._receipts = None

    def load(self, day):
        self._receipts = self._store.receipts_for(day)

    def render(self):
        if self._receipts is None:
            raise RuntimeError("load() must be called before render()")
        return "\n".join(receipt.summary() for receipt in self._receipts)
