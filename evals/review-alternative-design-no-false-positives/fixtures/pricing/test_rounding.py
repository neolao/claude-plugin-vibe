import unittest

from pricing.rounding import round_to_cents


class RoundToCentsTest(unittest.TestCase):
    def test_half_rounds_up(self):
        self.assertEqual(round_to_cents("1.005"), 101)

    def test_below_half_rounds_down(self):
        self.assertEqual(round_to_cents("1.004"), 100)

    def test_whole_amount(self):
        self.assertEqual(round_to_cents("2"), 200)
