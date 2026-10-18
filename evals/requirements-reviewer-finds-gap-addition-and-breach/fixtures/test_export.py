import unittest

from export import export_report


class ExportReportTest(unittest.TestCase):
    def test_csv_has_header_and_rows(self):
        rows = [{"date": "2026-03-02", "amount": 12.5, "label": "Coffee"}]
        name, body = export_report(rows, "2026-03")
        self.assertEqual(name, "report-2026-03.csv")
        self.assertIn("date,amount,label", body.decode())
        self.assertIn("Coffee", body.decode())


if __name__ == "__main__":
    unittest.main()
