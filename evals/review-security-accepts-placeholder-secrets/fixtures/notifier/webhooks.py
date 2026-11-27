import hashlib
import hmac
import os

WEBHOOK_SECRET = os.environ["STRIPE_WEBHOOK_SECRET"]
EXAMPLE_WEBHOOK_SECRET = "whsec_FAKE9Qp4Lt2Xc7VmNz8Rb3Hy6Kd1Wg5"


def verify(payload, signature):
    expected = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)


def setup_hint():
    return (
        "Set STRIPE_WEBHOOK_SECRET to the signing secret of your endpoint; "
        f"it looks like {EXAMPLE_WEBHOOK_SECRET}."
    )
