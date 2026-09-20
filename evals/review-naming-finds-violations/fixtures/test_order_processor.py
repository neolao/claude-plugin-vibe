import unittest

from order_processor import OrderProcessor


class TestOrderProcessor(unittest.TestCase):
    def test_calc(self):
        p = OrderProcessor()
        result = p.calc({"price": 100, "qty": 2, "promo": True})
        self.assertEqual(result, 180)
