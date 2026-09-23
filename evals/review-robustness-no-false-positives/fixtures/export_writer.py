import contextlib
import os


def export_orders(orders, path):
    """Called from the admin export endpoint; writes a CSV to disk."""
    tmp_path = f"{path}.tmp"
    try:
        with open(tmp_path, "w") as f:
            for order in orders:
                f.write(f"{order['id']},{order['total']}\n")
        os.replace(tmp_path, path)
    except Exception:
        with contextlib.suppress(OSError):
            os.remove(tmp_path)
        raise


def load_export_template(path):
    try:
        with open(path) as f:
            return f.read()
    except OSError as e:
        raise RuntimeError(f"failed to load export template at {path}") from e
