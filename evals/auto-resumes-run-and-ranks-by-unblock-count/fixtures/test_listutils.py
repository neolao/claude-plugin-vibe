import unittest

from listutils import first_of, is_even


class TestIsEven(unittest.TestCase):
    def test_returns_true_for_even_number(self):
        self.assertTrue(is_even(4))

    def test_returns_false_for_odd_number(self):
        self.assertFalse(is_even(3))


class TestFirstOf(unittest.TestCase):
    def test_returns_the_first_value(self):
        self.assertEqual(first_of([7, 8, 9]), 7)


if __name__ == "__main__":
    unittest.main()
