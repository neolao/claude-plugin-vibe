"""HTTP client for the supplier gateway; called from the polling loop."""
import json
from urllib import request

GATEWAY_URL = "https://gateway.example.test/orders/pending"


def fetch_pending():
    # open the gateway url
    with request.urlopen(GATEWAY_URL, timeout=10) as response:
        if response.status >= 400:
            raise RuntimeError(f"gateway answered {response.status}")
        return json.load(response)
