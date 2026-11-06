from datetime import date, timedelta

PERIOD_DAYS = {"monthly": 30, "yearly": 365}
GRACE_DAYS = 7


class Subscription:
    """A customer's recurring plan. Loaded and saved through SubscriptionRepository."""

    def __init__(self, subscription_id: str, customer_id: str, plan: str, period_end: date, status: str = "active"):
        self.subscription_id = subscription_id
        self.customer_id = customer_id
        self.plan = plan
        self._period_end = period_end
        self._status = status

    @property
    def status(self) -> str:
        return self._status

    @property
    def period_end(self) -> date:
        return self._period_end

    def renew(self, today: date) -> None:
        if self._status == "cancelled":
            raise ValueError(f"subscription {self.subscription_id} is cancelled")
        if self._period_end + timedelta(days=GRACE_DAYS) < today:
            self._status = "lapsed"
            return
        self._period_end = max(self._period_end, today) + timedelta(days=PERIOD_DAYS[self.plan])
        self._status = "active"

    def cancel(self) -> None:
        self._status = "cancelled"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Subscription) and other.subscription_id == self.subscription_id

    def __hash__(self) -> int:
        return hash(self.subscription_id)
