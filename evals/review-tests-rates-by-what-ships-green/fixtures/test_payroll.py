import unittest
from unittest.mock import patch

import payroll


class TestNetPay(unittest.TestCase):
    def test_net_pay_applies_tax_rate(self):
        with patch("payroll.net_pay", return_value=800.0):
            self.assertEqual(payroll.net_pay(1000, 0.2), 800.0)
