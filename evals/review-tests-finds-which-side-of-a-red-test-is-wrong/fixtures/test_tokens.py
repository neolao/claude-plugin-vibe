import unittest
from datetime import date

from tokens import Token, is_expired


class TestIsExpired(unittest.TestCase):
    def test_token_expiring_next_decade_is_valid(self):
        token = Token("abc", date(2030, 1, 1))
        self.assertFalse(is_expired(token))

    def test_token_expired_last_decade(self):
        token = Token("abc", date(2015, 1, 1))
        self.assertTrue(is_expired(token))
