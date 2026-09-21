from flask import Blueprint, jsonify, request

from order_repository import OrderRepository

bp = Blueprint("orders", __name__)
repo = OrderRepository()


@bp.route("/users/<user_id>/orders/<order_id>/close", methods=["POST"])
def close_order_route(user_id, order_id):
    # Business rule: orders over $500 need a manager approval flag before closing.
    order = repo.find_by_id(order_id)
    total = sum(item["qty"] * item["price"] for item in order["items"])
    if total > 500 and not request.args.get("approved"):
        return jsonify({"error": "needs approval"}), 403
    order["status"] = "closed"
    repo.save(order)
    return jsonify(order), 200
