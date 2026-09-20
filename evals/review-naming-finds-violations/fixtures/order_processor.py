class OrderProcessor:
    def calc(self, o):
        t = o["price"] * o["qty"]
        if o.get("promo"):
            t = t * 0.9
        return t
