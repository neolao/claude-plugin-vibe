import unittest
from datetime import date

from core.filenames import invoice_filename, parse_invoice_filename


class FilenamesTest(unittest.TestCase):
    def test_round_trip(self):
        name = invoice_filename("A1B2", date(2026, 3, 14))
        self.assertEqual(parse_invoice_filename(name), ("A1B2", date(2026, 3, 14)))

    def test_foreign_file_is_ignored(self):
        self.assertIsNone(parse_invoice_filename("notes.txt"))
