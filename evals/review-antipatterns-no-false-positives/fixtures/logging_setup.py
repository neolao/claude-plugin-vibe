import logging

logger = logging.getLogger("payments")
logger.setLevel(logging.INFO)


def log_charge(order):
    logger.info("charged order %s", order.id)
