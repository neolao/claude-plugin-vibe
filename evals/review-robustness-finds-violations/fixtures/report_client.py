import requests


def fetch_report(report_url):
    """Called from the nightly reporting job against a third-party API."""
    while True:
        response = requests.get(report_url)
        if response.status_code == 200:
            return response.json()
