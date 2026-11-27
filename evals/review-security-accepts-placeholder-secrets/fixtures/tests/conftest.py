import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

STUB_API_KEY = "pk_FAKE7Qm2Lx9VbN4rTw8Yz3HsKd6Pe1Ga"


class PostalStub(BaseHTTPRequestHandler):
    def do_POST(self):
        self.rfile.read(int(self.headers.get("Content-Length", 0)))
        status = 200 if self.headers.get("X-Postal-Key") == STUB_API_KEY else 401
        self.send_response(status)
        self.end_headers()

    def log_message(self, *args):
        pass


@pytest.fixture(scope="session")
def postal():
    server = HTTPServer(("127.0.0.1", 0), PostalStub)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield {"url": f"http://127.0.0.1:{server.server_port}/v1/messages", "api_key": STUB_API_KEY}
    server.shutdown()
