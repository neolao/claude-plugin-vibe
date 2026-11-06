"""Amount parsing for the supplier price lists."""
from decimal import Decimal, InvalidOperation

_SYMBOLS = ("€", "EUR", "$", "USD")


def parse_amount(text):
    """Return the amount in cents; accepts a currency symbol and a comma decimal; raises ValueError on a non-amount or a negative."""
    cleaned = _strip_currency(text).replace(",", ".")
    try:
        value = Decimal(cleaned)
    except InvalidOperation:
        raise ValueError(f"not an amount: {text!r}")
    if value < 0:
        raise ValueError(f"negative amount: {text!r}")
    # TODO(#231): JPY has no minor unit, the *100 is wrong for it
    return int(value * 100)


def _strip_currency(text):
    stripped = text.strip()
    for symbol in _SYMBOLS:
        stripped = stripped.replace(symbol, "")
    return stripped.strip()
