"""Tax on an order total. Used by the checkout and the invoice export."""


class TaxCalculator:
    def __init__(self, rates_source):
        self._rates_source = rates_source
        self._rates = {}

    def load_rates(self):
        self._rates = self._rates_source.fetch()

    def total(self, amount_cents, country):
        rate = self._rates.get(country, 0)
        return amount_cents + int(amount_cents * rate)
