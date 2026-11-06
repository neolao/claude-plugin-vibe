"""HTTP layer: a ThreadingHTTPServer, one thread per request."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from billing.checkout import checkout_total
from billing.model import Customer
from billing.notify import build_receipt
from billing.settlement import is_settled
from catalog.importer import price_of
from stock.inventory import reserve

customers: dict[str, Customer] = {}
orders = {}
invoices = {}
payments = {}


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
            # sku comes from the form field the clerk typed
            ok = reserve(body["sku"], int(body["qty"]))
            self._reply(200 if ok else 409, {"reserved": ok})
        elif self.path == "/checkout":
            customer = customers[body["customer_id"]]
            subtotal = sum(price_of(line["sku"]) * line["qty"] for line in body["lines"])
            self._reply(200, {"total": checkout_total(customer, subtotal)})
        elif self.path == "/payments":
            invoice = invoices[body["invoice_id"]]
            order = orders[invoice.order_id]
            received = payments.setdefault(invoice.id, [])
            received.append(body["payment"])
            receipt = build_receipt(order, invoice, customers)
            self._reply(200, {"settled": is_settled(invoice, received), "receipt": receipt})
        else:
            self._reply(404, {})


def serve(port=8080):
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
