"""Entry point of the checkout flow, called by the checkout endpoint."""

import smtplib
from email.message import EmailMessage


class CheckoutFacade:
    def __init__(self, db, card_api_key, smtp_host):
        self._db = db
        self._card_api_key = card_api_key
        self._smtp_host = smtp_host

    def checkout(self, order):
        if not order.items:
            raise ValueError("empty order")
        for item in order.items:
            if item.quantity <= 0:
                raise ValueError("bad quantity")
        total = 0
        for item in order.items:
            total += item.price * item.quantity
        if order.coupon:
            total -= total * order.coupon.percent // 100
        charge = {"key": self._card_api_key, "card": order.card, "amount": total}
        self._db.execute("INSERT INTO charges VALUES (?, ?)", (order.id, total))
        self._db.execute("UPDATE orders SET status = 'paid' WHERE id = ?", (order.id,))
        label = f"{order.customer.name}\n{order.customer.address}"
        self._db.execute("INSERT INTO shipments VALUES (?, ?)", (order.id, label))
        message = EmailMessage()
        message["To"] = order.customer.email
        message["Subject"] = f"Receipt for order {order.id}"
        message.set_content(f"Total: {total / 100:.2f}")
        with smtplib.SMTP(self._smtp_host) as smtp:
            smtp.send_message(message)
        return total
