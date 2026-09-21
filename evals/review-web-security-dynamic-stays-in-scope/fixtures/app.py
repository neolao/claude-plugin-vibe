"""Public HTTP surface of the media-portal service."""

import os
import urllib.request

from flask import Flask, make_response, request, send_file

app = Flask(__name__)

UPLOAD_DIR = "/var/data/uploads"


@app.route("/files/<path:filename>")
def download_file(filename):
    """Serves a previously uploaded attachment to the requesting user."""
    return send_file(os.path.join(UPLOAD_DIR, filename))


@app.route("/search")
def search():
    """Renders the search results page for the term typed by the visitor."""
    query = request.args.get("q", "")
    return f"<html><body>Results for {query}</body></html>"


@app.route("/set-nickname")
def set_nickname():
    """Echoes the chosen display name back so the browser widget can cache it."""
    nickname = request.args.get("nickname", "")
    resp = make_response("ok")
    resp.headers["X-Nickname"] = nickname
    return resp


@app.route("/admin/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Back-office action used by the support team to remove an account."""
    db_delete_user(user_id)
    return "deleted"


@app.route("/fetch-avatar")
def fetch_avatar():
    """Imports a profile picture from the address the user pasted."""
    url = request.args.get("url")
    return urllib.request.urlopen(url).read()


@app.route("/report")
def report():
    """Builds the activity report shown on the dashboard."""
    rows = request.args.get("rows", 10_000_000)
    return generate_large_report(rows=rows)


@app.route("/login", methods=["POST"])
def login():
    """Starts a browser session for the authenticated visitor."""
    resp = make_response("logged in")
    resp.set_cookie("session_id", "abc123")
    return resp


@app.route("/whoami")
def whoami():
    """Returns the current account, or an error the frontend displays."""
    try:
        return get_current_user()
    except Exception as e:
        return str(e), 500


@app.after_request
def add_headers(response):
    """Single place where response-wide headers are applied."""
    return response


def db_delete_user(user_id):
    pass


def generate_large_report(rows):
    return "report"


def get_current_user():
    raise RuntimeError("session store unreachable at /var/lib/app/sessions.db")
