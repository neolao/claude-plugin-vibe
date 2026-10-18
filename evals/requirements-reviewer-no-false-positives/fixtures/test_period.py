import unittest

from period import filter_period

ROWS = [
    {"date": "2026-03-01", "amount": 1, "label": "a"},
    {"date": "2026-03-10", "amount": 2, "label": "b"},
    {"date": "2026-03-31", "amount": 3, "label": "c"},
]


class FilterPeriodTest(unittest.TestCase):
    def test_bounds_are_included(self):
        kept = filter_period(ROWS, "2026-03-10", "2026-03-31")
        self.assertEqual([r["label"] for r in kept], ["b", "c"])

    def test_rows_outside_are_left_out(self):
        kept = filter_period(ROWS, "2026-03-02", "2026-03-09")
        self.assertEqual(kept, [])

    def test_reversed_period_is_refused(self):
        with self.assertRaises(ValueError):
            filter_period(ROWS, "2026-03-31", "2026-03-01")


if __name__ == "__main__":
    unittest.main()
