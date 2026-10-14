import json
import time
import urllib.request

DEFAULT_TIMEOUT = 5


class FetchError(Exception):
    pass


def http_get(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return response.read()


def fetch_json(url, timeout=DEFAULT_TIMEOUT):
    try:
        return json.loads(http_get(url, timeout))
    except (OSError, ValueError) as exc:
        raise FetchError(f"{url}: {exc}") from exc


def load_profile(user_id):
    return fetch_json(f"https://api.example.test/users/{user_id}")


def load_inventory(sku):
    return fetch_json(f"https://api.example.test/stock/{sku}", timeout=30)


def retry(operation, attempts=3, delay=0.5):
    last_error = None
    for _ in range(attempts):
        try:
            return operation()
        except FetchError as exc:
            last_error = exc
            time.sleep(delay)
    raise last_error


def refresh_profile_once(user_id):
    return retry(lambda: load_profile(user_id), attempts=1)


def refresh_inventory_patiently(sku):
    return retry(lambda: load_inventory(sku), attempts=5, delay=2)


def refresh_default(user_id):
    return retry(lambda: load_profile(user_id))
