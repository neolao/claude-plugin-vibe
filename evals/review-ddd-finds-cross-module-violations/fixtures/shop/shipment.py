import requests

from address import Address

CARRIER_API = "https://api.carrier.example/v2"


class ShipmentNotFound(Exception):
    pass


class Shipment:
    def __init__(self, shipment_id: str, cart_id: str, destination: Address, status: str = "pending"):
        self.shipment_id = shipment_id
        self.cart_id = cart_id
        self.destination = destination
        self.status = status

    def mark_dispatched(self) -> None:
        if self.status != "pending":
            raise ValueError(f"shipment {self.shipment_id} is already {self.status}")
        self.status = "dispatched"

    def estimate_delivery(self) -> str:
        resp = requests.get(
            f"{CARRIER_API}/estimates",
            params={"postcode": self.destination.postcode},
            timeout=5,
        )
        resp.raise_for_status()
        return resp.json()["date"]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Shipment) and other.shipment_id == self.shipment_id

    def __hash__(self) -> int:
        return hash(self.shipment_id)
