from decimal import Decimal

import pytest

from shop_api.domain.order import Order, OrderLine


def test_total_sums_line_subtotals():
    order = Order("o-1")
    order.add_line(OrderLine("sku-1", 2, Decimal("3.50")))
    assert order.total() == Decimal("7.00")


def test_submit_rejects_empty_order():
    with pytest.raises(ValueError):
        Order("o-2").submit()
