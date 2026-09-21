"""Application entry point."""

from adapters.postgres_gateway import PostgresGateway
from core.order_service import OrderService


def build_order_service():
    gateway = PostgresGateway()
    return OrderService(gateway)
