import logging

log = logging.getLogger(__name__)


def write_manifest(path, parcels) -> bool:
    """The end-of-day list the carrier's driver signs at pickup."""
    try:
        with open(path, "w") as out:
            for parcel in parcels:
                out.write(f"{parcel['id']},{parcel['service']}\n")
        return True
    except OSError:
        log.warning("could not write manifest %s", path, exc_info=True)
        return False
