from dataclasses import dataclass


@dataclass(frozen=True)
class Line:
    sku: str
    unit_price: float
    quantity: int


@dataclass(frozen=True)
class Cart:
    lines: list[Line]
    coupon_percent: int = 0  # 0 when the customer entered no coupon
