"""Signs rendered reports so partners can check they were not altered."""
import os

from Crypto.Hash import HMAC, SHA256


def sign(body):
    mac = HMAC.new(os.environ["REPORT_SIGNING_KEY"].encode(), digestmod=SHA256)
    mac.update(body.encode())
    return mac.hexdigest()
