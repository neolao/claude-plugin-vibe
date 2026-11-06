"""Amount parsing for the supplier price lists."""
from decimal import Decimal, InvalidOperation

_SYMBOLS = ("€", "EUR", "$", "USD")


def parse_amount(text):
    """Parse the amount from the text."""
    cleaned = _strip_currency(text).replace(",", ".")
    try:
        value = Decimal(cleaned)
    except InvalidOperation:
        raise ValueError(f"not an amount: {text!r}")
    if value < 0:
        raise ValueError(f"negative amount: {text!r}")
    return int(value * 100)


def _strip_currency(text):
    """Strip the currency symbol from the text."""
    stripped = text.strip()
    for symbol in _SYMBOLS:
        stripped = stripped.replace(symbol, "")
    return stripped.strip()
