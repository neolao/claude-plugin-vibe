import unittest

from listutils import is_even


class TestIsEven(unittest.TestCase):
    def test_returns_true_for_even_number(self):
        self.assertTrue(is_even(4))

    def test_returns_false_for_odd_number(self):
        self.assertFalse(is_even(3))


if __name__ == "__main__":
    unittest.main()
