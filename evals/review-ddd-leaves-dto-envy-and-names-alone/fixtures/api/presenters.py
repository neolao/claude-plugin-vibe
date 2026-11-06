# Shapes the account page reads. Filled from the domain, never written back.
from dataclasses import dataclass
from datetime import date

from subscriptions.subscription import Subscription


@dataclass
class SubscriptionResponse:
    id: str
    plan: str
    status: str
    period_end: str


def to_response(sub: Subscription) -> SubscriptionResponse:
    return SubscriptionResponse(
        id=sub.subscription_id,
        plan=sub.plan,
        status=_label(sub.status),
        period_end=_fmt(sub.period_end),
    )


def _fmt(d: date) -> str:
    return d.strftime("%d %B %Y")


def _label(s: str) -> str:
    return {"active": "Active", "lapsed": "Payment due", "cancelled": "Cancelled"}[s]
