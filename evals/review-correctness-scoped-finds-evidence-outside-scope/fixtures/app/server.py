"""HTTP layer: a ThreadingHTTPServer, one thread per request."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from catalog.prices import price_of
from orders.checkout import checkout_total
from orders.model import Address, Customer, Order
from orders.reservations import reserve

customers: dict[str, Customer] = {}


class Handler(BaseHTTPRequestHandler):
    def _body(self):
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length) or b"{}")

    def _reply(self, status, payload):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_POST(self):
        body = self._body()
        if self.path == "/reserve":
            # sku and qty come from the form fields the clerk typed
            ok = reserve(body["sku"], int(body["qty"]))
            self._reply(200 if ok else 409, {"reserved": ok})
        elif self.path == "/checkout":
            customer = customers[body["customer_id"]]
            address = Address(body["country"], body["postcode"])
            subtotal = sum(price_of(line["sku"]) * line["qty"] for line in body["lines"])
            order = Order(body["order_id"], customer, address, subtotal)
            self._reply(200, {"total": checkout_total(order)})
        else:
            self._reply(404, {})


def serve(port=8080):
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
