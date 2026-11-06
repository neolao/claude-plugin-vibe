# Called by the morning job that mails the finance team the orders unpaid for too long.
from dataclasses import dataclass
from datetime import date, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from orders.order_repository import LineRecord, OrderRecord


@dataclass(frozen=True)
class OverdueRow:
    order_id: str
    customer_id: str
    placed_on: date
    total_cents: int


class OverdueReportQuery:
    """Read side of the finance report: one row per overdue order, totals computed in SQL."""

    def __init__(self, session: Session):
        self._session = session

    def rows(self, today: date, days: int = 30) -> list[OverdueRow]:
        cutoff = today - timedelta(days=days)
        result = (
            self._session.query(
                OrderRecord.id,
                OrderRecord.customer_id,
                OrderRecord.placed_on,
                func.sum(LineRecord.qty * LineRecord.unit_cents),
            )
            .join(LineRecord, LineRecord.order_id == OrderRecord.id)
            .filter(OrderRecord.status == "open", OrderRecord.placed_on < cutoff)
            .group_by(OrderRecord.id)
            .order_by(OrderRecord.placed_on)
            .all()
        )
        return [OverdueRow(r[0], r[1], r[2], int(r[3])) for r in result]
