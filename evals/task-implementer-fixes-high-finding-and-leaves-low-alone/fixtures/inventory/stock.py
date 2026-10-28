"""Stock levels per product. Called from the warehouse screen."""


class Stock:
    def __init__(self):
        self._levels = {}

    def add(self, product, quantity):
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._levels[product] = self._levels.get(product, 0) + quantity

    def remove(self, product, quantity):
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._levels[product] = max(0, self.level(product) - quantity)

    def level(self, product):
        return self._levels.get(product, 0)

    def is_low(self, product):
        lvl = self.level(product)
        return lvl < 3
