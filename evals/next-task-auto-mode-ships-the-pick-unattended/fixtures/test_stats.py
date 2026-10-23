import unittest

from stats import average_total


class AverageTotalTest(unittest.TestCase):
    def test_average_of_three_order_totals(self):
        self.assertEqual(average_total([10, 20, 30]), 20)


if __name__ == "__main__":
    unittest.main()
