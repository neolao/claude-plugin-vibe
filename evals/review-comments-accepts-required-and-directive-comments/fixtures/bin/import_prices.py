#!/usr/bin/env python3
"""Imports a supplier price list given on the command line."""
import csv
import sys

from pricing.amounts import parse_amount


def main(path):
    """Print one `ref;cents` line per row of the CSV at `path`; exit 1 on the first bad amount."""
    with open(path, newline="") as handle:
        rows = csv.DictReader(handle, delimiter=";")
        for row in rows:
            try:
                cents = parse_amount(row["price"])
            except ValueError as error:
                sys.exit(f"{path}: {error}")
            # TODO: skip the rows the supplier marks as discontinued
            print(f"{row['ref']};{cents}")


if __name__ == "__main__":
    main(sys.argv[1])  # type: ignore[arg-type]  # noqa: E501
