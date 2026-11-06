from datetime import date

from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import Query, Session, declarative_base

from orders.order import Order
from pricing.money import Money

Base = declarative_base()


class OrderRecord(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True)
    customer_id = Column(String, nullable=False)
    placed_on = Column(Date, nullable=False)
    status = Column(String, nullable=False)


class LineRecord(Base):
    __tablename__ = "order_lines"

    order_id = Column(String, primary_key=True)
    sku = Column(String, primary_key=True)
    qty = Column(Integer, nullable=False)
    unit_cents = Column(Integer, nullable=False)


class OrderNotFound(Exception):
    pass


class OrderRepository:
    def __init__(self, session: Session):
        self._session = session

    def get(self, order_id: str) -> Order:
        record = self._session.get(OrderRecord, order_id)
        if record is None:
            raise OrderNotFound(order_id)
        return self._to_order(record)

    def open_orders(self) -> Query:
        return self._session.query(OrderRecord).filter(OrderRecord.status == "open")

    def save(self, order: Order) -> None:
        self._session.merge(OrderRecord(id=order.order_id, customer_id=order.customer_id, placed_on=order.placed_on, status=order.status))
        self._session.query(LineRecord).filter(LineRecord.order_id == order.order_id).delete()
        for line in order.lines:
            self._session.add(LineRecord(order_id=order.order_id, sku=line.sku, qty=line.qty, unit_cents=line.unit_price.cents))
        self._session.commit()

    def _to_order(self, record: OrderRecord) -> Order:
        order = Order(record.id, record.customer_id, record.placed_on, record.status)
        for line in self._session.query(LineRecord).filter(LineRecord.order_id == record.id):
            order.add_line(line.sku, line.qty, Money(line.unit_cents, "EUR"))
        return order
