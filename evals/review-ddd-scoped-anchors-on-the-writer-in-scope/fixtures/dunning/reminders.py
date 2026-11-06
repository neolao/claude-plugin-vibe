# Called by the nightly job that emails customers whose order is still unpaid.
from orders.order_repository import OrderRepository


def unpaid_order_notices(repo: OrderRepository, days: int = 7) -> list[str]:
    notices = []
    for row in repo.find_unpaid(days):
        notices.append(f"Order {row[0]} for customer {row[1]} is still unpaid (placed {row[6]})")
    return notices
