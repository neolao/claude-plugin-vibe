"""Domain records shared by the order modules."""
from dataclasses import dataclass


@dataclass
class Customer:
    id: str
    email: str
    loyal: bool = False


@dataclass
class Address:
    country: str
    postcode: str


@dataclass
class Order:
    id: str
    customer_id: str
    address: Address
    subtotal: float


# A customer account can be closed and removed from the directory; the
# orders it placed are kept for accounting.
CustomerDirectory = dict[str, Customer]
