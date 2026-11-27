import unittest

from export import export_report


class ExportReportTest(unittest.TestCase):
    def test_csv_has_header_and_rows(self):
        rows = [{"date": "2026-03-02", "amount": 12.5, "label": "coffee beans"}]
        name, body = export_report(rows, "2026-03")
        self.assertEqual(name, "report-2026-03.csv")
        self.assertIn("date,amount,label", body.decode())
        self.assertIn("Coffee Beans", body.decode())

    def test_csv_ends_with_the_total(self):
        rows = [
            {"date": "2026-03-02", "amount": 12.5, "label": "coffee"},
            {"date": "2026-03-03", "amount": 0.333, "label": "tea"},
        ]
        _, body = export_report(rows, "2026-03")
        self.assertTrue(body.decode().strip().endswith("total,12.83"))


if __name__ == "__main__":
    unittest.main()
