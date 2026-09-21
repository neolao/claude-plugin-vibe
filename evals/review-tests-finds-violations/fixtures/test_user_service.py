import unittest
from unittest.mock import MagicMock

from user_service import UserService

# Isolation: module-level mutable state shared across tests instead of being
# reset per test — results depend on test execution order and how many
# times the module has been exercised in this process.
_shared_state = {}


class TestUserService(unittest.TestCase):
    def setUp(self):
        # Fixture: a bare MagicMock with nothing configured beyond the one
        # value each test needs — it never exercises any real storage
        # behaviour (lookup semantics, missing keys, persistence), so it
        # cannot catch a real UserService/db integration bug.
        self.db = MagicMock()
        self.service = UserService(self.db)

    def test_get_user(self):
        # Over-mocked: the mock is configured to return a value, and the
        # test only checks that *some* result came back — it verifies the
        # mock echoes itself, not any UserService logic.
        self.db.get.return_value = {"id": 1, "active": True}
        result = self.service.get_user(1)
        # Assertion precision: assertIsNotNone tolerates any truthy value;
        # a get_user() that returned {"id": 999} instead would still pass.
        self.assertIsNotNone(result)

    def test_deactivate_user_marks_inactive(self):
        _shared_state["calls"] = _shared_state.get("calls", 0) + 1
        self.db.get.return_value = {"id": 1, "active": True}
        self.service.deactivate_user(1)
        self.assertEqual(_shared_state["calls"], 1)

    # Coverage gap: deactivate_user() raises ValueError when the user does
    # not exist in the db, but no test in this file exercises that branch.


class TestUserServiceInfrastructure(unittest.TestCase):
    def setUp(self):
        # Infrastructure: connects to a real database that is not available
        # in this environment. This isolated integration check cannot
        # complete here, and that inability is itself worth reporting
        # rather than silently skipping.
        import psycopg2

        self.conn = psycopg2.connect(host="localhost", dbname="app_test")

    def test_user_row_persists(self):
        cur = self.conn.cursor()
        cur.execute("SELECT 1")
        self.assertEqual(cur.fetchone()[0], 1)
