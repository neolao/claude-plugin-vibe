class InventoryService:
    def __init__(self, stock):
        self._stock = stock

    def reserve(self, sku, quantity):
        available = self._stock.get(sku, 0)
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if available < quantity:
            raise ValueError(f"insufficient stock for {sku}")
        self._stock[sku] = available - quantity
        return self._stock[sku]
