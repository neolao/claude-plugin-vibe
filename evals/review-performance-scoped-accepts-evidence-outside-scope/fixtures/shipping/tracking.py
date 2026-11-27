_latest = {}


def record_scan(tracking_number, status, scanned_at):
    previous = _latest.get(tracking_number)
    if previous is None or scanned_at > previous[1]:
        _latest[tracking_number] = (status, scanned_at)


def latest_status(tracking_number):
    entry = _latest.get(tracking_number)
    return entry[0] if entry else None


def forget_delivered(before):
    """Drops the parcels delivered before the given instant."""
    for tracking_number, (status, scanned_at) in list(_latest.items()):
        if status == "delivered" and scanned_at < before:
            del _latest[tracking_number]
