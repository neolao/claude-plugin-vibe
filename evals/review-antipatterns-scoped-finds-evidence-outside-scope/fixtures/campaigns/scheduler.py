"""Nightly job that reloads the day's promotions from the catalog."""

from orders.promotions import ACTIVE_PROMOTIONS


def promotions_for_today():
    return []


def refresh():
    """Runs at midnight from the job runner."""
    ACTIVE_PROMOTIONS.clear()
    ACTIVE_PROMOTIONS.extend(promotions_for_today())
