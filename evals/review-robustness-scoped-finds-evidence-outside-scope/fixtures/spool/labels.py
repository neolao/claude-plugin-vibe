from pathlib import Path

SPOOL_DIR = Path("/var/spool/parcels")


def open_for(parcel_id: str):
    """One label file per parcel, collected by the carrier's pickup script."""
    return open(SPOOL_DIR / f"{parcel_id}.zpl", "wb")
