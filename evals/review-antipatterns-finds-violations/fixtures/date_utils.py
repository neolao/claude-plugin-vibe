def parse_iso_date(value):
    # hand-rolled ISO-8601 parser duplicating datetime.fromisoformat /
    # dateutil.parser.isoparse
    year, month, day = value.split("-")
    return {"year": int(year), "month": int(month), "day": int(day)}


# The currency code is duplicated as a literal in several unrelated places
# (see pricing_rules.py, order_workflow.py) instead of one shared constant —
# changing it means touching every file that mentions "USD".
DEFAULT_CURRENCY = "USD"


def format_price(order):
    return f"{order['total']} USD"
