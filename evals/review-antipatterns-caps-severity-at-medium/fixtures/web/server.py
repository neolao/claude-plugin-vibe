"""HTTP entry point. One thread per request."""

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

from web.login import login
from web.logout import logout


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/login":
            login(self.headers["X-User"], self.headers["X-Token"])
        elif self.path == "/logout":
            logout(self.headers["X-Token"])
        self.send_response(204)
        self.end_headers()


def serve():
    ThreadingHTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
