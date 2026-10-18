import unittest

from pricing import loyalty_rate, price_order


class LoyaltyRateTest(unittest.TestCase):
    def test_above_threshold_gets_ten_percent(self):
        self.assertEqual(loyalty_rate(900), 0.10)

    def test_below_threshold_gets_nothing(self):
        self.assertEqual(loyalty_rate(100), 0.0)


class PriceOrderTest(unittest.TestCase):
    def test_price_without_loyalty(self):
        self.assertEqual(price_order({"total": 80.0}), 80.0)


if __name__ == "__main__":
    unittest.main()
