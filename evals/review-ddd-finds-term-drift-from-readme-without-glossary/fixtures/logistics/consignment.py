from dataclasses import dataclass


@dataclass(frozen=True)
class Parcel:
    parcel_id: str
    weight_grams: int


class Consignment:
    def __init__(self, consignment_id: str, carrier: str, status: str = "open"):
        self.consignment_id = consignment_id
        self.carrier = carrier
        self._parcels: list[Parcel] = []
        self._status = status

    def add_parcel(self, parcel: Parcel) -> None:
        if self._status != "open":
            raise ValueError(f"consignment {self.consignment_id} is closed")
        self._parcels.append(parcel)

    def close(self) -> None:
        if not self._parcels:
            raise ValueError(f"consignment {self.consignment_id} has no parcel")
        self._status = "closed"

    @property
    def parcels(self) -> tuple[Parcel, ...]:
        return tuple(self._parcels)

    @property
    def status(self) -> str:
        return self._status

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Consignment) and other.consignment_id == self.consignment_id

    def __hash__(self) -> int:
        return hash(self.consignment_id)
