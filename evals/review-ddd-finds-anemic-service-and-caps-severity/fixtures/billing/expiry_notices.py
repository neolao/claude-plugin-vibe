# Called by the nightly job that emails customers whose plan ends within a week.
from subscriptions.subscription_repository import SubscriptionRepository


def expiry_notices(repo: SubscriptionRepository, within_days: int = 7) -> list[tuple[str, str]]:
    notices = []
    for row in repo.find_expiring(within_days):
        notices.append((row[5], f"Your {row[2]} plan ends on {row[4]}"))
    return notices
