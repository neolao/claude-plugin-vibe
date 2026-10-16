"""Entry point of the invoicing tool: python -m cli.main <command>."""
import sys
from datetime import date

from billing.export import export_invoices_csv
from billing.invoices import render_invoice
from reminders.overdue import overdue_invoices
from reports.aging import aging_report


def main(argv):
    command = argv[1] if len(argv) > 1 else "help"
    invoices = load_invoices()
    if command == "export":
        export_invoices_csv(invoices, sys.stdout)
    elif command == "invoice":
        print(render_invoice(invoices[0]))
    elif command == "overdue":
        for invoice in overdue_invoices(invoices, date.today()):
            print(invoice["number"])
    elif command == "aging":
        print(aging_report(invoices, date.today()))
    else:
        print("usage: invoicing <export|invoice|overdue|aging>")
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
