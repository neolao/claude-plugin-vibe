from abc import ABC, abstractmethod


class OrderGatewayPort(ABC):
    """The persistence contract core depends on — owned here, in core, not
    by whichever adapter happens to implement it."""

    @abstractmethod
    def save(self, order_id: str, total_cents: int) -> None:
        """Persist the final total for an order. Implementations return
        nothing — core never sees a technology-specific result."""
