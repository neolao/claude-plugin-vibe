import json
import urllib.parse
import urllib.request


class CarrierClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def quote(self, weight_grams, country):
        query = urllib.parse.urlencode({"weight": weight_grams, "country": country})
        with urllib.request.urlopen(f"{self.base_url}/quotes?{query}", timeout=10) as response:
            return json.load(response)["price_cents"]
