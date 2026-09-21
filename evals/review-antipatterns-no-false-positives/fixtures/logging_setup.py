import logging

# Actually wired up and used by payment_gateway.py below — not a copied-in
# ritual with no reason that applies here.
logger = logging.getLogger("payments")
logger.setLevel(logging.INFO)


def log_charge(order):
    logger.info("charged order %s", order.id)
