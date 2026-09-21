import psycopg2  # a domain module importing a concrete DB driver

from adapters.postgres_gateway import PostgresGateway
from core.pricing import calculate_total


class OrderService:
    """Places an order: prices it and persists it."""

    def __init__(self):
        # core builds its own adapter — nothing outside wires this
        # dependency in, and there is no composition root anywhere else in
        # the codebase
        self.gateway = PostgresGateway()

    def place_order(self, order):
        total = calculate_total(order)

        # core executing SQL directly, bypassing the gateway port entirely —
        # violates ADR 002 (core never talks to the database directly)
        conn = psycopg2.connect("dbname=orders")
        conn.cursor().execute("INSERT INTO orders (total) VALUES (%s)", (total,))

        self.gateway.save(order, total)
        return total
