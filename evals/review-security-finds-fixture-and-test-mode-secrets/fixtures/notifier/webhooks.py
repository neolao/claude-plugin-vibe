import hashlib
import hmac
import os

WEBHOOK_SECRET = os.environ["STRIPE_WEBHOOK_SECRET"]
# Rotated on 2026-03-02 after the incident; kept so replay_backlog() can verify the events queued before the rotation.
OLD_WEBHOOK_SECRET = "whsec_FAKE9Qp4Lt2Xc7VmNz8Rb3Hy6Kd1Wg5"


def verify(payload, signature, secret=WEBHOOK_SECRET):
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)


def replay_backlog(events):
    return [event for event in events if verify(event.payload, event.signature, OLD_WEBHOOK_SECRET)]
