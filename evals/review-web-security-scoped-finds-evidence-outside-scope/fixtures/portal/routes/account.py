"""The signed-in visitor's own area."""

from flask import Blueprint, session

from portal import orders, users

bp = Blueprint("account", __name__)


@bp.route("/account/profile")
def profile():
    """The visitor's profile page."""
    return users.render_profile(session["user_id"])


@bp.route("/account/orders/<order_id>")
def order(order_id):
    """One order's detail page, opened from the visitor's order list."""
    return orders.render(order_id)
