"""Support back-office."""

from flask import Blueprint

from portal import users

bp = Blueprint("admin", __name__)


@bp.route("/admin/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Back-office action used by the support team to remove an account."""
    users.delete(user_id)
    return "deleted"
