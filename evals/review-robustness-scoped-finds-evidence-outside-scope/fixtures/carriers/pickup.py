import requests

PICKUPS_URL = "https://api.carrier.example.com/pickups"


def request_pickup(session: requests.Session, manifest_path, parcel_count: int):
    response = session.post(
        PICKUPS_URL,
        json={"manifest": str(manifest_path), "parcels": parcel_count},
        timeout=10,
    )
    response.raise_for_status()
