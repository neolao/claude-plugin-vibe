"""Domain events raised by order placement."""

from dataclasses import dataclass

from adapters.audit_log import AuditLog


@dataclass(frozen=True)
class OrderPlaced:
    order_id: str
    total_cents: int

    def publish(self) -> None:
        AuditLog().record(f"order {self.order_id} placed for {self.total_cents} cents")
