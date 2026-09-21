import psycopg2

from adapters.postgres_gateway import PostgresGateway
from core.pricing import calculate_total


class OrderService:
    """Places an order: prices it and persists it."""

    def __init__(self):
        self.gateway = PostgresGateway()

    def place_order(self, order):
        total = calculate_total(order)
        self.gateway.save(order, total)
        return total

    def ping_storage(self):
        return psycopg2.connect("dbname=orders").status
