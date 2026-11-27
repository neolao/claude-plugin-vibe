import unittest

from memo import Memoizer


class TestMemoizer(unittest.TestCase):
    def test_compute_returns_the_function_result(self):
        memo = Memoizer(lambda x: x * x)
        self.assertEqual(memo.compute(4), 16)
        self.assertIn(4, memo._cache)

    def test_compute_calls_the_function_once_per_input(self):
        calls = []

        def square(x):
            calls.append(x)
            return x * x

        memo = Memoizer(square)
        memo.compute(4)
        memo.compute(4)
        self.assertEqual(calls, [4])
