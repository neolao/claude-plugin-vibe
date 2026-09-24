import os

SUPPLIER_URL = os.environ.get("SUPPLIER_URL", "https://supplier.example.com/api")

# Seconds; set per environment.
SUPPLIER_TIMEOUT = (
    float(os.environ["SUPPLIER_TIMEOUT"]) if "SUPPLIER_TIMEOUT" in os.environ else None
)
