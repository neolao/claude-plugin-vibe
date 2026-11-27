import json
import urllib.request

POSTAL_URL = "https://api.postal.example/v1/messages"


def send(api_key, to, subject, body):
    payload = json.dumps({"to": to, "subject": subject, "body": body}).encode()
    request = urllib.request.Request(
        POSTAL_URL, data=payload, headers={"X-Postal-Key": api_key, "Content-Type": "application/json"}
    )
    return urllib.request.urlopen(request)
