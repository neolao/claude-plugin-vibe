from carriers.pickup import request_pickup
from shipping.manifest import write_manifest


def close_day(session, parcels, manifest_path):
    """Run by the scheduler at 18:00; the driver comes for the pickup after it."""
    write_manifest(manifest_path, parcels)
    request_pickup(session, manifest_path, len(parcels))
