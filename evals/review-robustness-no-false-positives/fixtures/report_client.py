import time

import requests


def fetch_report(report_url, max_attempts=5):
    """Called from the nightly reporting job against a third-party API.
    Bounded attempts with an exponential backoff and a per-request
    timeout."""
    last_error = None
    for attempt in range(max_attempts):
        try:
            response = requests.get(report_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            last_error = e
        if attempt < max_attempts - 1:
            time.sleep(2 ** attempt)
    raise RuntimeError(
        f"report fetch failed after {max_attempts} attempts: {report_url}"
    ) from last_error
