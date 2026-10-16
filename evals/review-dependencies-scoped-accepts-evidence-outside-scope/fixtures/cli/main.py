"""Entry point of the back-office: python -m cli.main <command>."""
import sys
from datetime import date

from tabulate import tabulate

from orders.pricing import Line
from reports.aging import aging_rows


def main(argv):
    command = argv[1] if len(argv) > 1 else "help"
    if command == "aging":
        rows = aging_rows(load_unpaid_orders())
        print(tabulate(rows, headers="keys", tablefmt="github"))
    else:
        print("usage: backoffice <aging>")
    return 0


def load_unpaid_orders():
    return [
        {
            "number": "O-2026-0001",
            "placed_on": date(2026, 3, 1),
            "lines": [Line("SKU-1", 1000, 2)],
        },
    ]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
