"""Entry point of the billing tool: python -m billing.cli <command>."""
import sys

from billing.checkout import checkout_total
from billing.export import export_orders_csv
from billing.invoices import render_invoice
from billing.refunds import refund_amount


def main(argv):
    command = argv[1] if len(argv) > 1 else "help"
    if command == "export":
        export_orders_csv(load_orders(), sys.stdout)
    elif command == "invoice":
        print(render_invoice(load_orders()[0]))
    elif command == "total":
        print(checkout_total(load_orders()[0]["lines"]))
    elif command == "refund":
        print(refund_amount(load_orders()[0], int(argv[2])))
    else:
        print("usage: billing <export|invoice|total|refund>")
    return 0


def load_orders():
    return [
        {
            "id": "A-1",
            "customer": "ACME",
            "lines": [{"sku": "P1", "unit_cents": 1250, "qty": 2}],
        },
    ]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
