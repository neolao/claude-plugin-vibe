# Called by the nightly renewal job and by the "renew now" button of the account page.
from datetime import date

from subscriptions.subscription import Subscription
from subscriptions.subscription_repository import SubscriptionRepository


class RenewSubscription:
    def __init__(self, subscriptions: SubscriptionRepository):
        self._subscriptions = subscriptions

    def execute(self, subscription_id: str, today: date) -> Subscription:
        sub = self._subscriptions.get(subscription_id)
        sub.renew(today)
        self._subscriptions.save(sub)
        return sub
