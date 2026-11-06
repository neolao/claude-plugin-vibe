"""Entry point of the nightly export."""
from exporter.client import Throttled, post_shipments
from exporter.payload import build


def export_day(shipments, log):
    payload = build(shipments)
    try:
        return post_shipments(payload)
    except Throttled:
        log.warning("partner throttled the export, left for the next run")
        return None
