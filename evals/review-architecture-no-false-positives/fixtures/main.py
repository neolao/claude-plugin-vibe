"""Composition root: the only place in the codebase that constructs a
concrete adapter and wires it into core."""

from adapters.postgres_gateway import PostgresGateway
from core.order_service import OrderService


def build_order_service():
    gateway = PostgresGateway()
    return OrderService(gateway)
