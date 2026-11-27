import unittest

from ledger import Ledger


class TestLedger(unittest.TestCase):
    def test_balance_sums_posted_amounts(self):
        ledger = Ledger()
        ledger.post(10, "rent")
        ledger.post(-4, "refund")
        self.assertEqual(ledger.balance(), 6)

    def test_memos_keep_posting_order(self):
        ledger = Ledger()
        ledger.post(value=10, memo="rent")
        ledger.post(value=3, memo="coffee")
        self.assertEqual(ledger.memos(), ["rent", "coffee"])
