# Called by the morning job that mails the finance team the orders unpaid for too long.
from datetime import date, timedelta

from orders.order_repository import OrderRecord, OrderRepository


def overdue_report(repo: OrderRepository, today: date, days: int = 30) -> list[str]:
    cutoff = today - timedelta(days=days)
    records = repo.open_orders().filter(OrderRecord.placed_on < cutoff).order_by(OrderRecord.placed_on).all()
    return [f"{r.id} — customer {r.customer_id}, placed {r.placed_on.isoformat()}" for r in records]
