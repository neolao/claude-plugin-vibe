"""Net pay of one employee for one month."""


def net_pay(gross, tax_rate):
    """Gross pay minus tax, rounded to the cent."""
    return round(gross * (1 - tax_rate), 2)
