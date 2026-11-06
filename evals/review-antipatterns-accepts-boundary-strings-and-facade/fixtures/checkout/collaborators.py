"""The five checkout steps."""


class OrderValidator:
    def validate(self, order):
        if not order.items:
            raise ValueError("empty order")


class Pricer:
    def price(self, order):
        return sum(item.price for item in order.items)


class PaymentGateway:
    def charge(self, order, total):
        pass


class Shipper:
    def ship(self, order):
        pass


class Mailer:
    def send_receipt(self, order, total):
        pass
