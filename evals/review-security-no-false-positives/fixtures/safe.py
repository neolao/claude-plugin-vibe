import json
import os
import subprocess
import sqlite3

import bcrypt
import yaml

API_KEY = os.environ["API_KEY"]


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()


def run_backup(directory):
    subprocess.run(["tar", "-czf", "backup.tar.gz", directory], shell=False)


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def load_plugin_config(config_path):
    """Reads the descriptor bundled with a customer-supplied plugin archive."""
    with open(config_path) as handle:
        return yaml.safe_load(handle)


def export_invoices(db_path, requesting_user):
    """Builds the invoice archive the support console offers to an agent."""
    conn = sqlite3.connect(db_path)
    return conn.execute(
        "SELECT * FROM invoices WHERE customer_id = ?", (requesting_user.customer_id,)
    ).fetchall()


def charge_for_order(customer, order_file):
    """Charges `customer`'s card for an order file uploaded by the partner's till."""
    with open(order_file) as handle:
        order = json.load(handle)
    total_cents = 0
    for line in order["lines"]:
        quantity = line["quantity"]
        if not isinstance(quantity, int) or not (0 < quantity <= MAX_LINE_QUANTITY):
            raise ValueError(f"quantity out of range: {quantity!r}")
        total_cents += CATALOGUE[line["sku"]] * quantity
    return payment_gateway.charge(customer.card_token, total_cents)
