import unittest

from inventory.stock import Stock


class StockTest(unittest.TestCase):
    def test_add_accumulates(self):
        stock = Stock()
        stock.add("bolt", 3)
        stock.add("bolt", 2)
        self.assertEqual(stock.level("bolt"), 5)

    def test_add_refuses_non_positive_quantity(self):
        with self.assertRaises(ValueError):
            Stock().add("bolt", 0)


if __name__ == "__main__":
    unittest.main()
