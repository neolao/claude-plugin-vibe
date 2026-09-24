# Called by the warehouse terminal when a packer scans a finished box.
from shipment_repository import ShipmentRepository


def dispatch_parcel(repo: ShipmentRepository, parcel_id: str) -> None:
    parcel = repo.get(parcel_id)
    parcel.mark_dispatched()
    repo.save(parcel)


def pending_parcels(repo: ShipmentRepository) -> list[str]:
    return [parcel.shipment_id for parcel in repo.find_pending()]
