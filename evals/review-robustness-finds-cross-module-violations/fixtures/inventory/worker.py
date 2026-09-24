import logging

from . import jobs
from .errors import SyncFailed

log = logging.getLogger(__name__)


def tick(app, skus):
    """Called by the scheduler thread every five minutes; the next tick retries."""
    try:
        jobs.run(app.conn, app.supplier, skus, app.cursor)
    except SyncFailed as exc:
        log.error("sync run failed: %s", exc)
