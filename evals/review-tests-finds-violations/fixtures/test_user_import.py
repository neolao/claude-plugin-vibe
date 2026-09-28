"""Unit tests for the nightly user import (called on the partner's CSV export)."""

import unittest

from user_import import parse_users

SAMPLE = "id,name\n1,alice\n"


class TestParseUsers(unittest.TestCase):
    def test_parse_users_reads_rows(self):
        self.assertEqual(parse_users(SAMPLE), [{"id": 1, "name": "alice"}])
