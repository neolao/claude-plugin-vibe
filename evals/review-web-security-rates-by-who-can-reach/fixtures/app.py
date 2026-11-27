"""Customer portal."""

import os
import sqlite3
from functools import wraps

from flask import Flask, abort, session

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

DB_PATH = "/var/data/portal.db"


def login_required(view):
    """Signed-in customers only."""

    @wraps(view)
    def guarded(*args, **kwargs):
        if "user_id" not in session:
            abort(401)
        return view(*args, **kwargs)

    return guarded


@app.route("/account/orders/<order_id>")
@login_required
def order(order_id):
    """One order's detail page, opened from the customer's order list."""
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT total_cents, address FROM orders WHERE id = ?",
        (order_id,),
    ).fetchone()
    if row is None:
        abort(404)
    return f"<html><body>{row[0]} cents to {row[1]}</body></html>"


@app.route("/admin/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Back-office action used by the support team to remove an account."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    return "deleted"


@app.route("/")
def home():
    """The landing page."""
    return "<html><body>media portal</body></html>"
