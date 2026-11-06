import os

DSN = os.environ.get("SHOP_DSN", "postgresql://localhost/shop")
SMTP_HOST = os.environ.get("SMTP_HOST", "localhost")
AUDIT_PATH = os.environ.get("AUDIT_PATH", "/var/log/shop/audit.log")
