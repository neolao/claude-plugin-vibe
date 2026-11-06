"""Composition root: builds the adapters and wires them into the service."""

import os

from adapters.postgres_gateway import PostgresGateway
from api.http import OrderApi
from core.order_service import OrderService
from notifications.smtp_notifier import SmtpNotifier


def build_api() -> OrderApi:
    service = OrderService(
        gateway=PostgresGateway(),
        notifier=SmtpNotifier(os.environ.get("SMTP_HOST", "localhost"), "shop@example.com"),
    )
    return OrderApi(service)
