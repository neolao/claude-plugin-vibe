"""Builds the payload of one day's shipments for the partner API."""
from datetime import datetime, timezone


def build(shipments):
    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")  # ISO 8601 basic form: the partner rejects the extended one
    return {
        "sentAt": stamp,
        "shipments": [
            {"ref": shipment.ref, "weightGrams": shipment.weight_grams}
            for shipment in shipments
        ],
    }
