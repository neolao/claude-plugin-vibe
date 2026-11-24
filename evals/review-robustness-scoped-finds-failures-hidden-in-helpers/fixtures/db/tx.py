import logging
from contextlib import contextmanager

log = logging.getLogger(__name__)


@contextmanager
def transaction(conn):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        log.exception("transaction rolled back")
