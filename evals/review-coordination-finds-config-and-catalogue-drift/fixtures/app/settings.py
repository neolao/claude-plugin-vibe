"""Settings read once at start-up."""
import os

PAYMENT_TIMEOUT_SECONDS = int(os.environ["PAYMENT_TIMEOUT_SECONDS"])
RETRY_LIMIT = int(os.environ.get("RETRY_LIMIT", "3"))
