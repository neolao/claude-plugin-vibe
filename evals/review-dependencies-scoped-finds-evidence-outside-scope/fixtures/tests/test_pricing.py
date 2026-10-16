from datetime import date

import pytest
from freezegun import freeze_time

from orders.pricing import Line, basket_total_cents
from reports.aging import aging_rows


@pytest.fixture
def two_lines():
    return [Line("SKU-1", 1000, 2), Line("SKU-2", 500, 1)]


def test_basket_total_applies_vat(two_lines):
    assert basket_total_cents(two_lines) == 3000


def test_basket_total_applies_discount_before_vat(two_lines):
    assert basket_total_cents(two_lines, discount_percent=10) == 2700


@freeze_time("2026-06-15")
def test_aging_counts_whole_months(two_lines):
    rows = aging_rows([{"number": "O-1", "placed_on": date(2026, 3, 1), "lines": two_lines}])
    assert rows[0]["months_open"] == 3
