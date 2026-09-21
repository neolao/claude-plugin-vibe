import tempfile
import time
import unittest

from calculator import Memoizer, add, divide, is_even


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Tautological: the expected value is derived with the exact same
        # `a + b` logic the implementation uses, so a subtly wrong add()
        # (e.g. one that returns a - b for negative b) would still pass as
        # long as it stays internally consistent with this formula.
        a, b = 2, 3
        expected = a + b
        self.assertEqual(add(a, b), expected)

    def test_divide_works(self):
        # Under-asserting: only checks that no exception was raised, never
        # asserts the actual quotient — a divide() that always returns 0
        # would pass this test.
        try:
            divide(10, 2)
        except Exception:
            self.fail("divide raised an exception")

    @unittest.skip
    def test_divide_by_zero(self):
        # Dead test code: skipped with no reason string explaining why, and
        # it is the only test covering the error path, so
        # "Missing negative cases" applies too — divide(x, 0) currently has
        # no active test verifying it raises ValueError.
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_memoizer_caches_internally(self):
        # Implementation-coupled: reaches into the private `_cache` dict
        # instead of asserting through the public compute() behaviour. A
        # pure refactor to a different caching structure (e.g. functools
        # lru_cache) breaks this test even though compute() still works.
        memo = Memoizer()
        memo.compute(4)
        self.assertIn(4, memo._cache)


class TestCalculatorIntegration(unittest.TestCase):
    def test_add_writes_result_to_disk(self):
        # Wrong level: a real filesystem write plus a real sleep inside what
        # this suite treats as a fast unit test — this is an
        # integration-level test hiding in the unit suite, slowing it down
        # and coupling it to disk I/O for no reason `is_even`-style pure
        # functions need.
        time.sleep(0.3)
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            f.write(str(add(2, 3)))
            path = f.name
        with open(path) as f:
            self.assertEqual(f.read(), "5")

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))
