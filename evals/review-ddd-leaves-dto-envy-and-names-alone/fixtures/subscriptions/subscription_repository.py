import sqlite3
from datetime import date

from subscriptions.subscription import Subscription

_COLUMNS = "id, customer_id, plan, period_end, status"


class SubscriptionNotFound(Exception):
    pass


class SubscriptionRepository:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get(self, subscription_id: str) -> Subscription:
        row = self._conn.execute(
            f"SELECT {_COLUMNS} FROM subscriptions WHERE id = ?", (subscription_id,)
        ).fetchone()
        if row is None:
            raise SubscriptionNotFound(subscription_id)
        return self._to_subscription(row)

    def find_expiring(self, within_days: int) -> list[Subscription]:
        rows = self._conn.execute(
            f"SELECT {_COLUMNS} FROM subscriptions"
            " WHERE status = 'active' AND period_end <= date('now', ?)",
            (f"+{within_days} days",),
        ).fetchall()
        return [self._to_subscription(row) for row in rows]

    def save(self, sub: Subscription) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO subscriptions (id, customer_id, plan, period_end, status)"
            " VALUES (?, ?, ?, ?, ?)",
            (sub.subscription_id, sub.customer_id, sub.plan, sub.period_end.isoformat(), sub.status),
        )
        self._conn.commit()

    def _to_subscription(self, row) -> Subscription:
        return Subscription(row[0], row[1], row[2], date.fromisoformat(row[3]), row[4])
