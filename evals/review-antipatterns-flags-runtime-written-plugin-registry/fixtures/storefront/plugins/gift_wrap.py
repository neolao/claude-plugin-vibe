from storefront.registry import plugin


@plugin("gift_wrap")
class GiftWrap:
    def adjust(self, cart):
        if cart.gift:
            cart.add_line("Gift wrapping", 450)
