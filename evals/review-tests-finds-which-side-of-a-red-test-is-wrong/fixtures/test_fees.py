import unittest

from fees import transfer_fee


class TestTransferFee(unittest.TestCase):
    def test_fee_is_two_percent(self):
        self.assertEqual(transfer_fee(100), 2.0)

    def test_fee_is_capped_at_five(self):
        self.assertEqual(transfer_fee(1000), 5.0)
