import os
import re
import urllib.request
from functools import wraps
from urllib.parse import urlparse

from flask import Flask, abort, make_response, request
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_DIR = os.path.realpath("/var/data/uploads")
ALLOWED_AVATAR_HOSTS = {"cdn.example.com"}


def require_admin(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if request.headers.get("X-Admin-Token") != os.environ.get("ADMIN_TOKEN"):
            abort(403)
        return view(*args, **kwargs)

    return wrapped


@app.route("/files/<path:filename>")
def download_file(filename):
    # Path traversal safe: the name is sanitized, then the resolved path is
    # re-checked to still be inside UPLOAD_DIR before it is served.
    safe_name = secure_filename(filename)
    full_path = os.path.realpath(os.path.join(UPLOAD_DIR, safe_name))
    if not full_path.startswith(UPLOAD_DIR + os.sep):
        abort(400)
    with open(full_path, "rb") as f:
        return f.read()


@app.route("/search")
def search():
    query = request.args.get("q", "")
    # XSS safe: user input is escaped before being embedded in HTML.
    return f"<html><body>Results for {escape(query)}</body></html>"


@app.route("/set-nickname")
def set_nickname():
    nickname = request.args.get("nickname", "")
    resp = make_response("ok")
    # Header injection safe: CR/LF and anything outside a safe character
    # set are stripped before the value reaches a response header.
    safe_nickname = re.sub(r"[^A-Za-z0-9 _-]", "", nickname)[:50]
    resp.headers["X-Nickname"] = safe_nickname
    return resp


@app.route("/admin/users/<user_id>/delete", methods=["POST"])
@require_admin
def delete_user(user_id):
    db_delete_user(user_id)
    return "deleted"


@app.route("/fetch-avatar")
def fetch_avatar():
    url = request.args.get("url", "")
    host = urlparse(url).hostname
    # SSRF safe: only an explicit allowlist of hosts can be fetched.
    if host not in ALLOWED_AVATAR_HOSTS:
        abort(400)
    return urllib.request.urlopen(url).read()


@app.route("/report")
def report():
    # DoS safe: the requested page size is clamped regardless of what the
    # client asks for.
    rows = min(int(request.args.get("rows", 100)), 500)
    return generate_report(rows=rows)


@app.route("/login", methods=["POST"])
def login():
    resp = make_response("logged in")
    # Cookies safe: HttpOnly, Secure, and SameSite are all set on the
    # session cookie.
    resp.set_cookie(
        "session_id", "abc123", httponly=True, secure=True, samesite="Strict"
    )
    return resp


@app.route("/whoami")
def whoami():
    try:
        return get_current_user()
    except Exception:
        # Info disclosure safe: a generic message is returned; the real
        # exception is only logged server-side.
        app.logger.exception("failed to resolve current user")
        return "unable to load user", 500


@app.after_request
def add_security_headers(response):
    # Security headers present: CSP, nosniff, frame options, and HSTS are
    # all set on every response.
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=63072000"
    return response


def db_delete_user(user_id):
    pass


def generate_report(rows):
    return "report"


def get_current_user():
    raise RuntimeError("internal detail")
