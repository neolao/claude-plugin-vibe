import time

import requests


def with_retries(call, attempts=None, delay=1.0):
    tried = 0
    while True:
        try:
            return call()
        except requests.RequestException:
            tried += 1
            if attempts is not None and tried >= attempts:
                raise
            time.sleep(delay)
