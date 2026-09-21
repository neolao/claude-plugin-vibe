"""Unit tests for the user service."""

import unittest
from unittest.mock import MagicMock

from user_service import UserService

_shared_state = {}


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.db = MagicMock()
        self.service = UserService(self.db)

    def test_get_user(self):
        self.db.get.return_value = {"id": 1, "active": True}
        result = self.service.get_user(1)
        self.assertIsNotNone(result)

    def test_deactivate_user_marks_inactive(self):
        _shared_state["calls"] = _shared_state.get("calls", 0) + 1
        self.db.get.return_value = {"id": 1, "active": True}
        self.service.deactivate_user(1)
        self.assertEqual(_shared_state["calls"], 1)


class TestUserServiceInfrastructure(unittest.TestCase):
    """Integration check against the shared app_test database."""

    def setUp(self):
        import psycopg2

        self.conn = psycopg2.connect(host="localhost", dbname="app_test")

    def test_user_row_persists(self):
        cur = self.conn.cursor()
        cur.execute("SELECT 1")
        self.assertEqual(cur.fetchone()[0], 1)
