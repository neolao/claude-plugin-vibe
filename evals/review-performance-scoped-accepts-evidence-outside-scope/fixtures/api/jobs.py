from datetime import datetime, timedelta, timezone

from shipping import tracking


def prune_scans():
    """Scheduled every night at 03:00."""
    tracking.forget_delivered(datetime.now(timezone.utc) - timedelta(days=7))
