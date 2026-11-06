# Called by the nightly job that emails customers whose order is still unpaid.
from orders.order_repository import OrderRepository


def unpaid_order_notices(repo: OrderRepository, days: int = 7) -> list[str]:
    notices = []
    for order in repo.find_unpaid(days):
        notices.append(f"Order {order.order_id} for customer {order.customer_id} is still unpaid")
    return notices
