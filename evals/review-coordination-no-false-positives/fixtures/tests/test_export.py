import tempfile
import unittest
from pathlib import Path

from reports.export import export_tickets

GOLDEN = Path(__file__).resolve().parent / "golden" / "export_sample.csv"


class Ticket:
    def __init__(self, reference, status, priority):
        self.reference = reference
        self.status = status
        self.priority = priority


class ExportTest(unittest.TestCase):
    def test_export_matches_golden_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "out.csv"
            export_tickets([Ticket("T-1", "open", "normal"), Ticket("T-2", "closed", "urgent")], path)
            self.assertEqual(path.read_text(), GOLDEN.read_text())
