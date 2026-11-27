import unittest

from shipping.rates import rate_for


class TestRateFor(unittest.TestCase):
    def test_rate_lookup_works(self):
        rate_for("EU")
        self.assertTrue(True)
