"""Back-office actions on marketing campaigns."""

from orders.promotions import ACTIVE_PROMOTIONS


def launch(promotion):
    """Called from the admin UI when a marketer publishes a promotion."""
    ACTIVE_PROMOTIONS.append(promotion)


def withdraw(promotion):
    """Called from the admin UI when a marketer pulls a promotion."""
    ACTIVE_PROMOTIONS.remove(promotion)
