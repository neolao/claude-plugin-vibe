def render_cart(items):
    return [f"{item['name']} x{item['quantity']}" for item in items]
