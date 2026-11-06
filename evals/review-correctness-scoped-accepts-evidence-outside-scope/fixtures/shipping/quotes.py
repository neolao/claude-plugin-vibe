"""Carrier quotes; the carrier table is loaded at startup."""
from dataclasses import dataclass

CARRIERS = {
    "FR": ("colis-express", 4.90),
    "BE": ("colis-express", 6.90),
    "DE": ("paketdienst", 7.50),
}


class UnservedCountry(Exception):
    pass


@dataclass
class Quote:
    carrier: str
    amount: float


def quote_for(address):
    """Quote for an address; raises UnservedCountry when no carrier serves it."""
    entry = CARRIERS.get(address.country)
    if entry is None:
        raise UnservedCountry(address.country)
    carrier, amount = entry
    return Quote(carrier, amount)
