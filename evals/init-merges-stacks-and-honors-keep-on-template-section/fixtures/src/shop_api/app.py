from decimal import Decimal

from fastapi import FastAPI, HTTPException

from shop_api.domain.order import Order, OrderLine

app = FastAPI(title="shop-api")
_orders: dict[str, Order] = {}


@app.post("/orders/{order_id}/lines")
def add_line(order_id: str, sku: str, quantity: int, unit_price: Decimal) -> dict:
    order = _orders.setdefault(order_id, Order(order_id))
    order.add_line(OrderLine(sku, quantity, unit_price))
    return {"order_id": order_id, "total": str(order.total())}


@app.post("/orders/{order_id}/submit")
def submit(order_id: str) -> dict:
    order = _orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="order not found")
    order.submit()
    return {"order_id": order_id, "status": order.status}
