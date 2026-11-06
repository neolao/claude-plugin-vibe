from dataclasses import dataclass


@dataclass(frozen=True)
class OrderPlaced:
    order_id: str
    customer_id: str
    skus: tuple[str, ...]
