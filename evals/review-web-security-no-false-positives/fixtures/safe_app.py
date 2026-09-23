"""Public HTTP surface of the media-portal service."""

import hmac
import os
import re
import secrets
import urllib.request
from functools import wraps
from urllib.parse import urlparse

from flask import Flask, abort, make_response, request
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_DIR = os.path.realpath("/var/data/uploads")
ALLOWED_AVATAR_HOSTS = {"cdn.example.com"}
ADMIN_TOKEN = os.environ["ADMIN_TOKEN"]


class _RefuseRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_avatar_opener = urllib.request.build_opener(_RefuseRedirect)


def require_admin(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        supplied = request.headers.get("X-Admin-Token", "")
        if not hmac.compare_digest(supplied, ADMIN_TOKEN):
            abort(403)
        return view(*args, **kwargs)

    return wrapped


@app.route("/files/<path:filename>")
def download_file(filename):
    safe_name = secure_filename(filename)
    full_path = os.path.realpath(os.path.join(UPLOAD_DIR, safe_name))
    if not full_path.startswith(UPLOAD_DIR + os.sep):
        abort(400)
    with open(full_path, "rb") as f:
        return f.read()


@app.route("/search")
def search():
    query = request.args.get("q", "")
    return f"<html><body>Results for {escape(query)}</body></html>"


@app.route("/set-nickname")
def set_nickname():
    nickname = request.args.get("nickname", "")
    resp = make_response("ok")
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
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_AVATAR_HOSTS:
        abort(400)
    return _avatar_opener.open(url, timeout=5).read()


@app.route("/report")
def report():
    rows = max(1, min(request.args.get("rows", 100, type=int), 500))
    return generate_report(rows=rows)


@app.route("/login", methods=["POST"])
def login():
    resp = make_response("logged in")
    resp.set_cookie(
        "session_id", secrets.token_urlsafe(32), httponly=True, secure=True, samesite="Strict"
    )
    return resp


@app.route("/whoami")
def whoami():
    try:
        return get_current_user()
    except Exception:
        app.logger.exception("failed to resolve current user")
        return "unable to load user", 500


@app.after_request
def add_security_headers(response):
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
