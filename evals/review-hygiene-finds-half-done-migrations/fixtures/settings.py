import os

DATABASE_URL = os.environ.get("DATABASE_URL", "orders.db")
PAYMENT_URL = os.environ["PAYMENT_URL"]
CARRIER_URL = os.environ["CARRIER_URL"]
