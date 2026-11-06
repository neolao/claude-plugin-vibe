from abc import ABC, abstractmethod


class OrderPersistenceError(Exception):
    """Raised when an order total cannot be persisted."""


class OrderGatewayPort(ABC):
    """The persistence contract core depends on."""

    @abstractmethod
    def save(self, order_id: str, total_cents: int) -> None:
        """Persist the final total for an order.

        Raises OrderPersistenceError when the store rejects the write.
        """

    @abstractmethod
    def totals_since(self, day: str) -> list[int]:
        """Totals of the orders placed on or after `day` (ISO date)."""


class NotifierPort(ABC):
    """The confirmation contract core depends on."""

    @abstractmethod
    def order_confirmed(self, order_id: str, total_cents: int) -> None:
        """Tell the customer the order is placed."""
