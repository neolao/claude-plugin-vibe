import unittest
from datetime import date

from ledger import Ledger


class TestLedger(unittest.TestCase):
    def test_balance_sums_posted_amounts(self):
        ledger = Ledger()
        ledger.post(10, f"rent {date.today().isoformat()}")
        ledger.post(-4, f"refund {date.today().isoformat()}")
        self.assertEqual(ledger.balance(), 6)

    def test_memos_keep_posting_order(self):
        ledger = Ledger()
        ledger.post(10, "rent")
        ledger.post(3, "coffee")
        self.assertEqual(ledger.memos(), ["rent", "coffee"])
