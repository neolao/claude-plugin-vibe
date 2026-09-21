import time

import requests


def fetch_report(report_url, max_attempts=5):
    """Called from the nightly reporting job against a third-party API.
    Bounded attempts with an exponential backoff and a per-request
    timeout."""
    for attempt in range(max_attempts):
        response = requests.get(report_url, timeout=10)
        if response.status_code == 200:
            return response.json()
        time.sleep(2 ** attempt)
    raise RuntimeError(f"report fetch failed after {max_attempts} attempts: {report_url}")
