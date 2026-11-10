"""Called from the customer-support console and the nightly billing job."""
from datetime import date

from .subscription import Subscription


def handle_support_request(sub: Subscription, action: str, today: date) -> str:
    if action == "pause":
        sub.pause(today)
    elif action == "resume":
        sub.resume()
    elif action == "cancel":
        sub.cancel(today)
    return sub.label()


def nightly_billing(subs: list, today: date) -> list:
    billed = []
    for sub in subs:
        if sub.can_be_billed():
            billed.append(sub.id)
        elif sub.is_trial and sub.trial_ends is not None and sub.trial_ends <= today:
            sub.start_paid()
    return billed


def reactivate_from_import(sub: Subscription) -> None:
    sub.is_cancelled = False
    sub.is_active = True
    sub.is_paused = False
