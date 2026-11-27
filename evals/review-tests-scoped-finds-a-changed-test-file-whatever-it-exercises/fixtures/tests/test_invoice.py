import unittest

from billing.invoice import invoice_total


class TestInvoiceTotal(unittest.TestCase):
    def test_sums_quantity_times_unit_price(self):
        self.assertEqual(invoice_total([(2, 10.0), (1, 4.5)]), 24.5)
