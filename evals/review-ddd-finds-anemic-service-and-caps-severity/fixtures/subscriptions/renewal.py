# Called by the nightly renewal job and by the "renew now" button of the account page.
from datetime import date, timedelta

from subscriptions.subscription import Subscription
from subscriptions.subscription_repository import SubscriptionRepository

PERIOD_DAYS = {"monthly": 30, "yearly": 365}
GRACE_DAYS = 7


class RenewalService:
    def __init__(self, subscriptions: SubscriptionRepository):
        self._subscriptions = subscriptions

    def renew(self, subscription_id: str, today: date) -> Subscription:
        sub = self._subscriptions.get(subscription_id)
        if sub.status == "cancelled":
            raise ValueError(f"subscription {sub.subscription_id} is cancelled")
        if sub.period_end + timedelta(days=GRACE_DAYS) < today:
            sub.status = "lapsed"
        else:
            sub.period_end = max(sub.period_end, today) + timedelta(days=PERIOD_DAYS[sub.plan])
            sub.status = "active"
        self._subscriptions.save(sub)
        return sub
