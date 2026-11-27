_last_seen = {}


def record_heartbeat(device_id, seen_at, firmware):
    _last_seen[device_id] = (seen_at, firmware)


def status(device_id):
    entry = _last_seen.get(device_id)
    if entry is None:
        return {"state": "unknown"}
    return {"state": "online", "seen_at": entry[0], "firmware": entry[1]}
