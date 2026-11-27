import unittest
from datetime import date

from tokens import Token, is_expired


class TestIsExpired(unittest.TestCase):
    def test_token_is_valid_before_its_expiry_day(self):
        token = Token("abc", date(2030, 1, 1))
        self.assertFalse(is_expired(token, today=date(2029, 12, 31)))

    def test_token_is_expired_after_its_expiry_day(self):
        token = Token("abc", date(2030, 1, 1))
        self.assertTrue(is_expired(token, today=date(2030, 1, 2)))
