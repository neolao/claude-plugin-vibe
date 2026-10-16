"""Entry point of the invoicing tool: python -m cli.main <command>."""
import sys
from datetime import date

from billing import export_invoices_csv
from reports.summary import monthly_summary


def main(argv):
    command = argv[1] if len(argv) > 1 else "help"
    invoices = load_invoices()
    if command == "export":
        export_invoices_csv(invoices, sys.stdout)
    elif command == "summary":
        print(monthly_summary(invoices))
    else:
        print("usage: invoicing <export|summary>")
    return 0


def load_invoices():
    return [
        {
            "number": "2026-0001",
            "customer": "ACME",
            "total_cents": 125000,
            "issued": date(2026, 9, 1),
        },
    ]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
