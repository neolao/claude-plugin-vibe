import json
import unittest

from exports import REGISTRY


class JsonExportTest(unittest.TestCase):
    def test_renders_rows_as_json(self):
        body = REGISTRY["json"].render([{"date": "2026-03-01", "amount_cents": 1250, "label": "Coffee"}])
        self.assertEqual(json.loads(body)[0]["label"], "Coffee")

    def test_file_name_uses_month_and_extension(self):
        self.assertEqual(REGISTRY["json"].file_name("2026-03"), "report-2026-03.json")


if __name__ == "__main__":
    unittest.main()
