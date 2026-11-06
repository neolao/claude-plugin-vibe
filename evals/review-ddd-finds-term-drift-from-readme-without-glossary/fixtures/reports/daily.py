# Called by the end-of-day job that mails the warehouse manager.
from logistics.consignment_repository import ConsignmentRepository


def daily_summary(repo: ConsignmentRepository, day: str) -> list[str]:
    lines = []
    for batch in repo.find_closed_on(day):
        grams = sum(p.weight_grams for p in batch.parcels)
        lines.append(f"Batch {batch.consignment_id} ({batch.carrier}): {len(batch.parcels)} parcels, {grams / 1000:.1f} kg")
    return lines
