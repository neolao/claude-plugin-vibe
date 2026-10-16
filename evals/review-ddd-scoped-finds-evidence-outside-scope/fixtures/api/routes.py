import sqlite3

from flask import Blueprint, jsonify

from checkout.customer_orders import CustomerOrders
from orders.order_repository import OrderRepository

bp = Blueprint("orders", __name__)
customer_orders = CustomerOrders(OrderRepository(sqlite3.connect("shop.db", check_same_thread=False)))


@bp.get("/customers/<customer_id>/orders")
def list_customer_orders(customer_id: str):
    orders = customer_orders.for_customer(customer_id)
    return jsonify([{"id": o.order_id, "status": o.status, "total_cents": o.total().cents} for o in orders])
