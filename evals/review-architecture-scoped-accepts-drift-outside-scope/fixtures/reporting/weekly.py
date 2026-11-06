"""Weekly finance report over the stored totals, with the promo spend of the week."""

from adapters.postgres_gateway import PostgresGateway

PROMO_PERCENT = {"WELCOME10": 10, "SPRING15": 15}


def promo_spend(subtotal_cents: int, code: str) -> int:
    return min(subtotal_cents * PROMO_PERCENT.get(code, 0) // 100, 5_000)


def build_weekly_report(day: str) -> str:
    totals = PostgresGateway().totals_since(day)
    spend = sum(promo_spend(total, "WELCOME10") for total in totals)
    return f"since {day}: {len(totals)} orders, {sum(totals)} cents, {spend} cents of promo"
