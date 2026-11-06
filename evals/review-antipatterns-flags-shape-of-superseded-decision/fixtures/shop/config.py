"""Settings of the shop service."""

DATABASE_URL = "postgresql://shop@db.internal/shop"
REQUEST_TIMEOUT_SECONDS = 5

QUEUE_URL = "amqp://queue.internal/shop"
QUEUE_PREFETCH = 16
QUEUE_RETRY_SECONDS = 30
