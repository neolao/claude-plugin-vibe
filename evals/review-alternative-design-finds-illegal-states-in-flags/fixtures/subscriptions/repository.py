"""Maps `Subscription` to the `subscriptions` table, one boolean column per flag."""
from .subscription import Subscription


def load(row: dict) -> Subscription:
    return Subscription(
        id=row["id"],
        plan=row["plan"],
        is_trial=row["is_trial"],
        is_active=row["is_active"],
        is_paused=row["is_paused"],
        is_cancelled=row["is_cancelled"],
        trial_ends=row["trial_ends"],
        paused_since=row["paused_since"],
        cancelled_on=row["cancelled_on"],
    )


def save(sub: Subscription) -> dict:
    return {
        "id": sub.id,
        "plan": sub.plan,
        "is_trial": sub.is_trial,
        "is_active": sub.is_active,
        "is_paused": sub.is_paused,
        "is_cancelled": sub.is_cancelled,
        "trial_ends": sub.trial_ends,
        "paused_since": sub.paused_since,
        "cancelled_on": sub.cancelled_on,
    }
