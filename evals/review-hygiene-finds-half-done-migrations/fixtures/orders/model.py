from dataclasses import dataclass


@dataclass
class Order:
    id: str
    customer_id: str
    total_cents: int
    weight_grams: int
    country: str
    shipping_cents: int = 0
