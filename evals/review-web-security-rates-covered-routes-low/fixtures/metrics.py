"""Metrics sidecar scraped by the Prometheus agent on the host."""

from http.server import BaseHTTPRequestHandler, HTTPServer

COUNTERS = {"orders_rendered": 0, "users_deleted": 0}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/metrics":
            self.send_error(404)
            return
        body = "\n".join(f"{name} {value}" for name, value in COUNTERS.items())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body.encode())

    def do_POST(self):
        """Zeroes every counter, used by the nightly rollover job."""
        if self.path != "/metrics/reset":
            self.send_error(404)
            return
        for name in COUNTERS:
            COUNTERS[name] = 0
        self.send_response(204)
        self.end_headers()


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 9100), Handler).serve_forever()
