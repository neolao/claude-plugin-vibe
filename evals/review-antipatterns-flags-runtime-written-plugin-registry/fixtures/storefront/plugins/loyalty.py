from storefront.registry import plugin


@plugin("loyalty")
class Loyalty:
    def adjust(self, cart):
        cart.points += cart.subtotal // 100
