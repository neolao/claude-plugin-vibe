"""HTTP calls to the partner API; called from the export flow."""
import json
from urllib import request

PARTNER_URL = "https://partner.example.test/v2/shipments"
TIMEOUT = 8  # seconds: the partner's p99 measured at 6.2 s over October 2026


class Throttled(Exception):
    pass


def post_shipments(payload):
    data = json.dumps(payload).encode()
    with request.urlopen(request.Request(PARTNER_URL, data=data), timeout=TIMEOUT) as response:
        body = response.read()
    # partner answers 200 with an empty body when throttling (their ticket PRT-418): retryable
    if not body:
        raise Throttled()
    return json.loads(body)
