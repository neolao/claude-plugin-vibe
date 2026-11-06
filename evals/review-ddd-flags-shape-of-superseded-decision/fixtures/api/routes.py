import sqlite3

from flask import Blueprint, jsonify

from orders.order_repository import OrderRepository

bp = Blueprint("orders", __name__)
orders = OrderRepository(sqlite3.connect("shop.db", check_same_thread=False))


@bp.get("/buyers/<buyer_id>/orders")
def list_buyer_orders(buyer_id: str):
    found = orders.find_for_customer(buyer_id)
    return jsonify([
        {"id": o.order_id, "buyer_id": o.customer_id, "status": o.status, "total_cents": o.total().cents}
        for o in found
    ])
