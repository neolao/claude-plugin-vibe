import re
import unittest
from pathlib import Path

from core.currencies import ALLOWED_CURRENCIES

SCHEMA = Path(__file__).resolve().parent.parent / "db" / "schema.sql"
CURRENCY_CHECK = re.compile(r"CHECK \(currency IN \(([^)]*)\)\)")


class SchemaTest(unittest.TestCase):
    def test_currency_check_lists_the_allowed_currencies(self):
        listed = CURRENCY_CHECK.search(SCHEMA.read_text()).group(1)
        codes = {code.strip().strip("'") for code in listed.split(",")}
        self.assertEqual(codes, set(ALLOWED_CURRENCIES))
