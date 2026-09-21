def export_orders(orders, path):
    """Called from the admin export endpoint; writes a CSV to disk. The
    `with` block guarantees the file is closed even if a write raises."""
    with open(path, "w") as f:
        for order in orders:
            f.write(f"{order['id']},{order['total']}\n")


def load_export_template(path):
    try:
        with open(path) as f:
            return f.read()
    except OSError as e:
        raise RuntimeError(f"failed to load export template at {path}") from e
