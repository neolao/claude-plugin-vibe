"""Places an order: prices it and stores it. Imported first by main.py."""

from dataclasses import dataclass

from adapters.postgres_gateway import PostgresGateway
from core.ports import OrderGatewayPort
from core.pricing import calculate_total


@dataclass(frozen=True)
class OrderRecord:
    order_id: str
    total_cents: int


class OrderService:
    def __init__(self, gateway: OrderGatewayPort | None = None) -> None:
        self._gateway = gateway or PostgresGateway()

    def place(self, order_id: str, line_amounts_cents: list[int]) -> OrderRecord:
        total = calculate_total(line_amounts_cents)
        self._gateway.save(order_id, total)
        return OrderRecord(order_id, total)
