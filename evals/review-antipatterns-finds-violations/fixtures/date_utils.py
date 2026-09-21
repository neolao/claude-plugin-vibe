"""Date and price helpers shared by the ordering code."""


def parse_iso_date(value):
    year, month, day = value.split("-")
    return {"year": int(year), "month": int(month), "day": int(day)}


DEFAULT_CURRENCY = "USD"


def format_price(order):
    return f"{order['total']} USD"
