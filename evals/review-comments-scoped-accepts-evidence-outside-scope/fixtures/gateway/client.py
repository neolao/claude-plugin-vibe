"""HTTP client for the supplier gateway; called from the polling loop."""
import json
from urllib import error, request

GATEWAY_URL = "https://gateway.example.test/orders/pending"


def fetch_pending():
    # open the gateway url
    try:
        with request.urlopen(GATEWAY_URL, timeout=10) as response:
            return json.load(response)
    except error.HTTPError as http_error:
        raise RuntimeError(f"gateway answered {http_error.code}") from http_error
