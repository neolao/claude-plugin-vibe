import requests


def get_json(session: requests.Session, url: str, timeout=None):
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()
