"""Renders the cart page. Called on every cart page load and after every quantity change."""

from shop.pricing import total


def render(cart):
    return {
        "lines": [{"sku": line.sku, "quantity": line.quantity, "price": line.unit_price} for line in cart.lines],
        "total": total(cart),
    }
