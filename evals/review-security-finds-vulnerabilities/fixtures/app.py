import json
import subprocess
import hashlib
import sqlite3

import yaml

AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE7Q2Z9K3M8P1R"


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()


def run_backup(filename):
    subprocess.run("tar -czf backup.tar.gz " + filename, shell=True)


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def load_plugin_config(config_path):
    """Reads the descriptor bundled with a customer-supplied plugin archive."""
    with open(config_path) as handle:
        return yaml.load(handle)


def export_all_invoices(db_path, requesting_user):
    """Builds the invoice archive the support console offers to an agent."""
    conn = sqlite3.connect(db_path)
    return conn.execute("SELECT * FROM invoices").fetchall()


def charge_for_order(customer, order_file):
    """Charges `customer`'s card for an order file uploaded by the partner's till."""
    with open(order_file) as handle:
        order = json.load(handle)
    return payment_gateway.charge(customer.card_token, order["total_cents"])
