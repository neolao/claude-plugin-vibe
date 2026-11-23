import json
import urllib.request


class PaymentGateway:
    def __init__(self, base_url):
        self.base_url = base_url

    def charge(self, customer_id, amount_cents):
        return self._post("/charges", {"customer": customer_id, "amount": amount_cents})

    def refund(self, customer_id, amount_cents):
        return self._post("/refunds", {"customer": customer_id, "amount": amount_cents})

    def _post(self, path, body):
        request = urllib.request.Request(
            self.base_url + path,
            data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            return json.load(response)
