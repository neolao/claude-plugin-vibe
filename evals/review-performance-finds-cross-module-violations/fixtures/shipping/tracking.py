_latest = {}


def record_scan(tracking_number, status, scanned_at):
    previous = _latest.get(tracking_number)
    if previous is None or scanned_at > previous[1]:
        _latest[tracking_number] = (status, scanned_at)


def latest_status(tracking_number):
    entry = _latest.get(tracking_number)
    return entry[0] if entry else None
