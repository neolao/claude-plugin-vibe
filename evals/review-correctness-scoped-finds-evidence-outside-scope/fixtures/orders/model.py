"""Domain records shared by the order modules."""
from dataclasses import dataclass


@dataclass
class Customer:
    id: str
    loyal: bool = False


@dataclass
class Address:
    country: str
    postcode: str


@dataclass
class Order:
    id: str
    customer: Customer
    address: Address
    subtotal: float
