"""Entry point of the checkout flow, called by the checkout endpoint."""


class CheckoutFacade:
    def __init__(self, validator, pricer, gateway, shipper, mailer):
        self._validator = validator
        self._pricer = pricer
        self._gateway = gateway
        self._shipper = shipper
        self._mailer = mailer

    def checkout(self, order):
        self._validator.validate(order)
        total = self._pricer.price(order)
        self._gateway.charge(order, total)
        self._shipper.ship(order)
        self._mailer.send_receipt(order, total)
        return total
