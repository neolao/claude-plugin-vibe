"""Places an order: prices it for the customer's tier and stores it."""

from repositories.order_repository import OrderRepository
from services.pricing import policy_for


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def place(self, order_id: str, line_amounts_cents: list[int], customer_tier: str) -> int:
        total = policy_for(customer_tier).total(line_amounts_cents)
        self._repository.save(order_id, total)
        return total
