def export_orders(orders, path):
    """Called from the admin export endpoint; writes a CSV to disk."""
    f = open(path, "w")
    for order in orders:
        f.write(f"{order['id']},{order['total']}\n")
    f.close()


def load_export_template(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        raise Exception("failed to load template")
