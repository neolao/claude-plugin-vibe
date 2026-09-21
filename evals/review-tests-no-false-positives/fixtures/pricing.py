class PricingService:
    def __init__(self, tax_rate_provider):
        self._tax_rate_provider = tax_rate_provider

    def total_with_tax(self, subtotal, region):
        rate = self._tax_rate_provider.rate_for(region)
        return round(subtotal * (1 + rate), 2)
