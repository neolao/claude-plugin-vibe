# Called by the nightly job that emails customers whose shipment is late.
from shipment_repository import ShipmentRepository


def late_shipment_notices(repo: ShipmentRepository, days: int = 7) -> list[str]:
    notices = []
    for row in repo.find_overdue(days):
        notices.append(f"Shipment {row[0]} to {row[4]} is running late (sent {row[6]})")
    return notices
