from datetime import date


class Subscription:
    """A customer's recurring plan. Loaded and saved through SubscriptionRepository."""

    def __init__(self, subscription_id: str, customer_id: str, plan: str, status: str, period_end: date):
        self.subscription_id = subscription_id
        self.customer_id = customer_id
        self.plan = plan
        self.status = status
        self.period_end = period_end

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Subscription) and other.subscription_id == self.subscription_id

    def __hash__(self) -> int:
        return hash(self.subscription_id)
