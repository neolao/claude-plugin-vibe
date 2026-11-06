"""Composition root: builds the adapters and wires them into the service."""

from adapters.postgres_gateway import PostgresGateway
from adapters.smtp_notifier import SmtpNotifier
from core.order_service import OrderService


def build_service() -> OrderService:
    return OrderService(gateway=PostgresGateway(), notifier=SmtpNotifier())
