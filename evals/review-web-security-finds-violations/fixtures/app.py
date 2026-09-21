import os
import urllib.request

from flask import Flask, make_response, request, send_file

app = Flask(__name__)

UPLOAD_DIR = "/var/data/uploads"


@app.route("/files/<path:filename>")
def download_file(filename):
    # Path traversal: filename is joined directly into the upload directory
    # with no normalization or containment check, so "../../etc/passwd" (or
    # an encoded variant) escapes UPLOAD_DIR.
    return send_file(os.path.join(UPLOAD_DIR, filename))


@app.route("/search")
def search():
    query = request.args.get("q", "")
    # XSS: the query string is reflected straight into the HTML response
    # with no escaping, so "<script>...</script>" executes in the victim's
    # browser.
    return f"<html><body>Results for {query}</body></html>"


@app.route("/set-nickname")
def set_nickname():
    nickname = request.args.get("nickname", "")
    resp = make_response("ok")
    # Header injection: user input is written directly into a response
    # header with no sanitization, so embedded CR/LF can inject extra
    # headers or split the response.
    resp.headers["X-Nickname"] = nickname
    return resp


@app.route("/admin/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    # Access control: this destructive admin action has no authentication
    # or authorization check at all — any caller can delete any user.
    db_delete_user(user_id)
    return "deleted"


@app.route("/fetch-avatar")
def fetch_avatar():
    url = request.args.get("url")
    # SSRF: the server fetches an attacker-controlled URL with no allowlist,
    # so it can be pointed at internal services or the cloud metadata
    # endpoint (e.g. http://169.254.169.254/).
    return urllib.request.urlopen(url).read()


@app.route("/report")
def report():
    rows = request.args.get("rows", 10_000_000)
    # DoS: an expensive report-generation operation with no size cap or
    # rate limit — a client can request an unbounded number of rows.
    return generate_large_report(rows=rows)


@app.route("/login", methods=["POST"])
def login():
    resp = make_response("logged in")
    # Cookies: the session cookie is set without HttpOnly, Secure, or
    # SameSite, so it is readable by JS (XSS-stealable) and sent
    # cross-site/over plain HTTP.
    resp.set_cookie("session_id", "abc123")
    return resp


@app.route("/whoami")
def whoami():
    try:
        return get_current_user()
    except Exception as e:
        # Info disclosure: the raw exception message (which includes an
        # internal file path) is returned straight to the client.
        return str(e), 500


@app.after_request
def add_headers(response):
    # Security headers: this hook exists but never sets anything — no CSP,
    # X-Content-Type-Options, X-Frame-Options, or HSTS on any response.
    return response


def db_delete_user(user_id):
    pass


def generate_large_report(rows):
    return "report"


def get_current_user():
    raise RuntimeError("session store unreachable at /var/lib/app/sessions.db")
