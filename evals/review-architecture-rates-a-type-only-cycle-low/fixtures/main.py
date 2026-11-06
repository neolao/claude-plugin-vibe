"""Entry point: builds the invoice of an order and prints its delivery estimate."""

import sys
from datetime import date

from billing.invoice import build_invoice
from shipping.schedule import eta_for


def main() -> int:
    invoice = build_invoice("A-1001", [1990, 2490], "DE")
    print(f"{invoice.order_id}: {invoice.total_cents} cents, delivered by {eta_for(invoice, date.today())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
