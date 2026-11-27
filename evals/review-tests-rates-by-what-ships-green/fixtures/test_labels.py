import unittest

from labels import pay_slip_label


class TestPaySlipLabel(unittest.TestCase):
    def test_label_joins_employee_and_month(self):
        self.assertEqual(
            pay_slip_label("Ada Lovelace", "2026-03"),
            "Pay slip - Ada Lovelace - 2026-03",
        )

    def test_label_strips_surrounding_spaces(self):
        self.assertEqual(
            pay_slip_label("  Ada Lovelace ", "2026-03"),
            "Pay slip - Ada Lovelace - 2026-03",
        )
