import unittest

from order_repository import OrderRepository


class TestOrderRepository(unittest.TestCase):
    def test_calculate_discounted_total_applies_promo_discount(self):
        repo = OrderRepository({})
        result = repo.calculate_discounted_total(
            {"price": 100, "quantity": 2, "has_promo": True}
        )
        self.assertEqual(result, 180)

    def test_is_active_returns_false_when_order_missing(self):
        repo = OrderRepository({})
        self.assertFalse(repo.is_active("missing"))
