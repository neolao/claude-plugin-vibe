import requests

DEFAULT_TIMEOUT = 10  # seconds


def get_json(session: requests.Session, url: str, timeout=DEFAULT_TIMEOUT):
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()
