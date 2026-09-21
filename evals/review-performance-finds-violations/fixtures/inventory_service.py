import json


def has_conflicting_reservation(new_reservation, existing_reservations):
    """Called from the POST /reservations request handler for every new
    booking, scanning the warehouse's full reservation list each time."""
    for other in existing_reservations:
        if other["warehouse"] == new_reservation["warehouse"] and other["slot"] == new_reservation["slot"]:
            return True
    return False


def load_warehouse_config(path):
    """Called synchronously from the reservations request handler on every
    request to read the warehouse's slot rules."""
    with open(path) as f:
        raw = f.read()
    return json.loads(raw)
