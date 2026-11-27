from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def price(self, invoice):
        raise NotImplementedError


class StandardPricing(PricingStrategy):
    def price(self, invoice):
        return sum(line["amount"] for line in invoice["lines"])


def price_invoice(invoice):
    return StandardPricing().price(invoice)
