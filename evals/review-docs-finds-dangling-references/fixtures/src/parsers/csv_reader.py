"""CSV statement reader: one Transaction per data row."""

import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    date: str
    label: str
    amount: float
    currency: str


def read(path):
    with open(path, newline="") as handle:
        for row in csv.DictReader(handle):
            yield Transaction(row["date"], row["label"], float(row["amount"]), row["currency"])
