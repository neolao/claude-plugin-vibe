import json
import os
import urllib.request

POSTAL_URL = "https://api.postal.example/v1/messages"
POSTAL_API_KEY = os.environ["POSTAL_API_KEY"]


def send(to, subject, body, api_key=POSTAL_API_KEY, url=POSTAL_URL):
    payload = json.dumps({"to": to, "subject": subject, "body": body}).encode()
    request = urllib.request.Request(
        url, data=payload, headers={"X-Postal-Key": api_key, "Content-Type": "application/json"}
    )
    return urllib.request.urlopen(request)
