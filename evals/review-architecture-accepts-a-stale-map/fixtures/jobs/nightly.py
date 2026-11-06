"""Nightly reconciliation: sums yesterday's order totals into the figure finance expects."""

import sys
from datetime import date, timedelta

from adapters.postgres_gateway import PostgresGateway


def main() -> int:
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    totals = PostgresGateway().totals_since(yesterday)
    print(f"{yesterday}: {len(totals)} orders, {sum(totals)} cents")
    return 0


if __name__ == "__main__":
    sys.exit(main())
