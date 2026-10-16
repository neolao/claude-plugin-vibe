"""Amount formatting for the printed reports."""


def format_amount(cents):
    return f"{cents / 100:.2f} EUR"
