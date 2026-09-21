"""Unit tests for the calculator module."""

import tempfile
import time
import unittest

from calculator import Memoizer, add, divide, is_even


class TestCalculator(unittest.TestCase):
    def test_add(self):
        a, b = 2, 3
        expected = a + b
        self.assertEqual(add(a, b), expected)

    def test_divide_works(self):
        try:
            divide(10, 2)
        except Exception:
            self.fail("divide raised an exception")

    @unittest.skip
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_memoizer_caches_internally(self):
        memo = Memoizer()
        memo.compute(4)
        self.assertIn(4, memo._cache)


class TestCalculatorIntegration(unittest.TestCase):
    def test_add_writes_result_to_disk(self):
        time.sleep(0.3)
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            f.write(str(add(2, 3)))
            path = f.name
        with open(path) as f:
            self.assertEqual(f.read(), "5")

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))
