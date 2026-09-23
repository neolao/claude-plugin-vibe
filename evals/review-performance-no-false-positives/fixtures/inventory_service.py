import json


def has_conflicting_reservation(new_reservation, reservations_by_slot):
    """Called from the POST /reservations request handler for every new
    booking. `reservations_by_slot` is a dict keyed by (warehouse, slot),
    maintained incrementally by the caller."""
    key = (new_reservation["warehouse"], new_reservation["slot"])
    return key in reservations_by_slot


def load_warehouse_config(path):
    """Loaded once at process startup, before the server starts accepting
    requests, and kept in memory for the life of the process."""
    with open(path) as f:
        raw = f.read()
    return json.loads(raw)
