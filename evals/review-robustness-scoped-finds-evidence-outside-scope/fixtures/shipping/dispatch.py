from carriers.http import get_json
from spool import labels

CARRIER_API = "https://api.carrier.example.com"


def dispatch_parcel(session, parcel):
    """Called by the scanner thread for each parcel scanned at the dock."""
    rate = get_json(session, f"{CARRIER_API}/rates/{parcel['service']}")
    label = labels.open_for(parcel["id"])
    label.write(render_label(parcel, rate))
    label.close()
    return {"id": parcel["id"], "cost_cents": rate["cents"]}


def render_label(parcel, rate):
    return f"{parcel['id']} {parcel['address']} {rate['cents']}\n".encode()
