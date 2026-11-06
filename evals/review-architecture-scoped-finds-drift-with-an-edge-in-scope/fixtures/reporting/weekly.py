"""Weekly finance report over the stored totals."""

from adapters.postgres_gateway import PostgresGateway


def build_weekly_report(day: str) -> str:
    totals = PostgresGateway().totals_since(day)
    return f"since {day}: {len(totals)} orders, {sum(totals)} cents"
