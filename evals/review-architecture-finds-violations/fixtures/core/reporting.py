import psycopg2


def monthly_totals(month):
    """Figures the month's revenue for the finance dashboard."""
    conn = psycopg2.connect("dbname=orders")
    rows = conn.cursor().execute(
        "SELECT SUM(total) FROM orders WHERE month = %s", (month,)
    )
    return rows
