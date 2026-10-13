"""Application entry point."""

import os

from adapters.postgres_gateway import PostgresGateway
from adapters.smtp_notifier import SmtpNotifier
from core.order_service import OrderService


def build_order_service():
    gateway = PostgresGateway(os.environ["DB_DSN"])
    notifier = SmtpNotifier(os.environ["SMTP_HOST"], "orders@example.com")
    return OrderService(gateway, notifier)
