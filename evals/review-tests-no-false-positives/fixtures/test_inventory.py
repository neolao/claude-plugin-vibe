import unittest

from inventory import InventoryService


class TestInventoryService(unittest.TestCase):
    def setUp(self):
        # Realistic fixture: representative starting stock for two distinct
        # skus, not a bare mock — exercises the real dict-backed storage.
        self.service = InventoryService(stock={"sku-1": 10, "sku-2": 0})

    def test_reserve_deducts_from_stock(self):
        remaining = self.service.reserve("sku-1", 3)
        self.assertEqual(remaining, 7)

    def test_reserve_raises_when_insufficient_stock(self):
        with self.assertRaises(ValueError):
            self.service.reserve("sku-2", 1)

    def test_reserve_raises_for_non_positive_quantity(self):
        with self.assertRaises(ValueError):
            self.service.reserve("sku-1", 0)


class TestInventoryServiceIsolation(unittest.TestCase):
    def setUp(self):
        # Fresh instance per test — no shared mutable state across tests,
        # so results never depend on execution order.
        self.service = InventoryService(stock={"sku-1": 5})

    def test_independent_reservation(self):
        remaining = self.service.reserve("sku-1", 2)
        self.assertEqual(remaining, 3)
