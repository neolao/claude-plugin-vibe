"""Composition root: builds the adapter and wires it into the service."""

from core.order_service import OrderService
from adapters.postgres_gateway import PostgresGateway


def build_service() -> OrderService:
    return OrderService(gateway=PostgresGateway())
