from dataclasses import dataclass


@dataclass(frozen=True)
class Parcel:
    parcel_id: str
    weight_grams: int


class Batch:
    def __init__(self, batch_id: str, carrier: str, status: str = "open"):
        self.batch_id = batch_id
        self.carrier = carrier
        self._parcels: list[Parcel] = []
        self._status = status

    def add_parcel(self, parcel: Parcel) -> None:
        if self._status != "open":
            raise ValueError(f"batch {self.batch_id} is closed")
        self._parcels.append(parcel)

    def close(self) -> None:
        if not self._parcels:
            raise ValueError(f"batch {self.batch_id} has no parcel")
        self._status = "closed"

    @property
    def parcels(self) -> tuple[Parcel, ...]:
        return tuple(self._parcels)

    @property
    def status(self) -> str:
        return self._status

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Batch) and other.batch_id == self.batch_id

    def __hash__(self) -> int:
        return hash(self.batch_id)
