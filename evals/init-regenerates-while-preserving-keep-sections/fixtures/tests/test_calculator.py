from acme_widgets.calculator import apply_tax, discounted_total


def test_discounted_total_applies_percentage_discount():
    assert discounted_total(10.0, 2, discount_percent=10) == 18.0


def test_apply_tax_adds_percentage():
    assert apply_tax(100.0, 20) == 120.0
