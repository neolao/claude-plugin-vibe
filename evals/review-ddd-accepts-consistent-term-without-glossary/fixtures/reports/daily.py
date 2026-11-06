# Called by the end-of-day job that mails the warehouse manager.
from logistics.batch_repository import BatchRepository


def daily_summary(repo: BatchRepository, day: str) -> list[str]:
    lines = []
    for batch in repo.find_closed_on(day):
        grams = sum(p.weight_grams for p in batch.parcels)
        lines.append(f"Batch {batch.batch_id} ({batch.carrier}): {len(batch.parcels)} parcels, {grams / 1000:.1f} kg")
    return lines
