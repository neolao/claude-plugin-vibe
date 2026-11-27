"""Builds the media-portal application."""

import os

from flask import Flask, abort, request, session

from portal import storage
from portal.routes import account, admin, files

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.before_request
def require_login():
    """Signed-in visitors only on the account area, support staff only on the back-office."""
    if request.path.startswith("/account/") and "user_id" not in session:
        abort(401)
    if request.path.startswith("/admin/"):
        if "user_id" not in session:
            abort(401)
        if session.get("role") != "admin":
            abort(403)


@app.after_request
def add_headers(response):
    """Single place where response-wide headers are applied."""
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "same-origin"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    return response


@app.route("/export")
def export():
    """Builds the activity export shown on the dashboard."""
    rows = int(request.args.get("rows", 1000))
    return storage.render_export(rows)


app.register_blueprint(account.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(files.bp)
