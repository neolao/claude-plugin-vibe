"""Domain records shared by the billing modules."""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Customer:
    id: str
    email: str
    loyal: bool = False


@dataclass
class Order:
    id: str
    customer_id: str
    status: str
    shipped: bool = False
    paid_at: datetime | None = None


@dataclass
class Invoice:
    id: str
    order_id: str
    total: float


@dataclass
class Payment:
    invoice_id: str
    amount: float
    received_at: datetime = field(default_factory=datetime.utcnow)


# A customer account can be closed and removed from the directory; the
# orders and invoices it produced are kept for accounting.
CustomerDirectory = dict[str, Customer]
