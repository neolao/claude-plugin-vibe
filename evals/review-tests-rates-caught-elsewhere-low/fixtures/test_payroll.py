import unittest

from payroll import net_pay


class TestNetPay(unittest.TestCase):
    def test_net_pay_rounds_to_the_cent(self):
        self.assertEqual(net_pay(1000, 0.2133), 786.7)

    def test_net_pay_with_no_tax_is_the_gross(self):
        self.assertEqual(net_pay(1234.56, 0), 1234.56)

    @unittest.skip("duplicate of test_net_pay_rounds_to_the_cent, tracked in #214")
    def test_net_pay_rounding(self):
        self.assertEqual(net_pay(1000, 0.2133), 786.7)
