"""Human-readable formatting helpers."""


def format_currency(amount: float, currency: str = "EUR") -> str:
    """Format a numeric amount as a currency string, e.g. '12.50 EUR'."""
    return f"{amount:.2f} {currency}"
