"""HTTP layer: a ThreadingHTTPServer, one thread per request."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from inventory.stock import LOCK
from orders.checkout import checkout_total
from orders.model import Address, Customer, Order
from orders.receipt import build_receipt
from orders.reservations import reserve
from shipping.quotes import UnservedCountry

customers: dict[str, Customer] = {}
orders: dict[str, Order] = {}


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
            with LOCK:
                ok = reserve(body["sku"], int(body["qty"]))
            self._reply(200 if ok else 409, {"reserved": ok})
        elif self.path == "/checkout":
            customer = customers.get(body["customer_id"])
            if customer is None:
                self._reply(404, {"error": "unknown customer"})
                return
            address = Address(body["country"], body["postcode"])
            order = Order(body["order_id"], customer.id, address, float(body["subtotal"]))
            try:
                total = checkout_total(order, customer)
            except UnservedCountry as e:
                self._reply(422, {"error": f"no carrier serves {e}"})
                return
            orders[order.id] = order
            self._reply(200, {"total": total})
        elif self.path == "/receipt":
            order = orders.get(body["order_id"])
            if order is None or order.customer_id not in customers:
                self._reply(404, {"error": "unknown order or customer"})
                return
            self._reply(200, build_receipt(order, customers))
        else:
            self._reply(404, {})


def serve(port=8080):
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
