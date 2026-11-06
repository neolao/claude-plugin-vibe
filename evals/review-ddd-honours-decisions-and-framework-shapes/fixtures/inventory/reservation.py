# Reserves the stock of each ordered SKU. Handles OrderPlaced in the request that placed the order.
from orders.events import OrderPlaced


class StockReservation:
    def __init__(self, stock: dict[str, int]):
        self._stock = stock

    def on_order_placed(self, event: OrderPlaced) -> None:
        for sku in event.skus:
            self._stock[sku] = self._stock.get(sku, 0) - 1
