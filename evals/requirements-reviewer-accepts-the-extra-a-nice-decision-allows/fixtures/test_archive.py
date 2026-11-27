import unittest
from datetime import date

from archive import Ledger, archive_old, register
from scheduler import JOBS

ROWS = [
    {"id": 1, "date": date(2024, 2, 1), "amount": 10},
    {"id": 2, "date": date(2024, 4, 1), "amount": 20},
    {"id": 3, "date": date(2026, 1, 1), "amount": 30},
]


class ArchiveOldTest(unittest.TestCase):
    def test_moves_rows_older_than_the_limit(self):
        ledger = Ledger(ROWS)
        moved = archive_old(ledger, date(2026, 3, 15))
        self.assertEqual(moved, 1)
        self.assertEqual([r["id"] for r in ledger.archive], [1])
        self.assertEqual([r["id"] for r in ledger.live], [2, 3])
        self.assertEqual(ledger.last_moved_ids, [1])

    def test_dry_run_moves_nothing(self):
        ledger = Ledger(ROWS)
        self.assertEqual(archive_old(ledger, date(2026, 3, 15), dry_run=True), 1)
        self.assertEqual(ledger.archive, [])
        self.assertEqual(len(ledger.live), 3)

    def test_logs_a_summary(self):
        with self.assertLogs("archive", level="INFO") as logs:
            archive_old(Ledger(ROWS), date(2026, 3, 15))
        self.assertEqual(logs.output, ["INFO:archive:archived 1 transactions"])

    def test_registers_a_nightly_job(self):
        register(Ledger(ROWS))
        self.assertEqual(JOBS[-1][0], 2)


if __name__ == "__main__":
    unittest.main()
