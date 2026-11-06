from datetime import datetime


class Order:
    """An order and the four facts of its life. Built by the checkout flow."""

    def __init__(self, order_id, total_cents):
        self.order_id = order_id
        self.total_cents = total_cents
        self.is_paid = False
        self.is_shipped = False
        self.is_cancelled = False
        self.is_refunded = False
        self.paid_at = None
        self.shipped_at = None
        self.cancelled_at = None
        self.refunded_at = None

    def pay(self, now=None):
        if self.is_cancelled:
            raise ValueError("cancelled order cannot be paid")
        if self.is_paid:
            raise ValueError("order already paid")
        self.is_paid = True
        self.paid_at = now or datetime.utcnow()

    def ship(self, now=None):
        if not self.is_paid:
            raise ValueError("unpaid order cannot ship")
        if self.is_cancelled:
            raise ValueError("cancelled order cannot ship")
        if self.is_shipped:
            raise ValueError("order already shipped")
        self.is_shipped = True
        self.shipped_at = now or datetime.utcnow()

    def cancel(self, now=None):
        if self.is_shipped:
            raise ValueError("shipped order cannot be cancelled")
        if self.is_cancelled:
            raise ValueError("order already cancelled")
        self.is_cancelled = True
        self.cancelled_at = now or datetime.utcnow()

    def refund(self, now=None):
        if not self.is_paid:
            raise ValueError("unpaid order cannot be refunded")
        if self.is_refunded:
            raise ValueError("order already refunded")
        if not self.is_cancelled and not self.is_shipped:
            raise ValueError("only a cancelled or shipped order is refunded")
        self.is_refunded = True
        self.refunded_at = now or datetime.utcnow()
