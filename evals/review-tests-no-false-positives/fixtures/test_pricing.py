import unittest
from unittest.mock import Mock

from pricing import PricingService


class TestPricingService(unittest.TestCase):
    def test_total_with_tax_applies_provided_rate(self):
        tax_provider = Mock()
        tax_provider.rate_for.return_value = 0.2
        service = PricingService(tax_provider)

        result = service.total_with_tax(100, "US")

        self.assertEqual(result, 120.0)

    def test_total_with_tax_rounds_to_cents(self):
        tax_provider = Mock()
        tax_provider.rate_for.return_value = 0.0725
        service = PricingService(tax_provider)

        result = service.total_with_tax(19.99, "CA")

        self.assertEqual(result, 21.44)
