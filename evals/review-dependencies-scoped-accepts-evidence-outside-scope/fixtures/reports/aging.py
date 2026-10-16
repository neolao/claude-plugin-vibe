"""Receivables aging: how long each unpaid basket has been waiting. Run monthly."""
from datetime import date

from dateutil.relativedelta import relativedelta

from orders.pricing import basket_total_cents


def aging_rows(unpaid_orders, today: date | None = None):
    today = today or date.today()
    rows = []
    for order in unpaid_orders:
        age = relativedelta(today, order["placed_on"])
        rows.append(
            {
                "order": order["number"],
                "months_open": age.years * 12 + age.months,
                "total_cents": basket_total_cents(order["lines"], order.get("discount_percent", 0)),
            }
        )
    return rows
