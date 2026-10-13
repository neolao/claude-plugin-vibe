from abc import ABC, abstractmethod


class OrderGatewayPort(ABC):
    """The persistence contract core depends on."""

    @abstractmethod
    def save(self, order_id: str, total_cents: int) -> None:
        """Persist the final total for an order."""


class NotifierPort(ABC):
    """How core tells a customer something happened."""

    @abstractmethod
    def order_confirmed(self, order_id: str, total_cents: int) -> None:
        """Tell the customer their order was confirmed."""
