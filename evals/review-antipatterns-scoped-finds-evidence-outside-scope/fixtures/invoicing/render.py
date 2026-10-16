"""Lines of the PDF invoice."""


def amount_line(label, cents):
    return f"{label}: {cents / 100:.2f} EUR"
