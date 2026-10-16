"""Amount formatting shared by the exports and the reports."""


def format_amount(cents):
    return f"{cents / 100:.2f} EUR"
