"""Delivery rates by zone, in euros."""

RATES = {"FR": 4.9, "EU": 9.5, "WORLD": 24.0}


def rate_for(zone):
    """Delivery rate of a zone code."""
    if zone not in RATES:
        raise KeyError(f"unknown zone {zone}")
    return RATES[zone]
