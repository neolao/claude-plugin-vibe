"""Audit trail of recorded payments, appended by the async payment worker."""
import asyncio
import logging

logger = logging.getLogger(__name__)

_pending = set()


async def append_audit_line(store, payment):
    try:
        await asyncio.wait_for(store.append(payment), timeout=5)
    except Exception:
        logger.exception("audit line lost for invoice %s", payment.invoice_id)


def _done(task):
    _pending.discard(task)
    if not task.cancelled():
        task.exception()


async def record_payment(store, payment):
    """Writing the audit line is intentionally fire-and-forget: the payment
    is already committed and the audit store is not on the critical path."""
    task = asyncio.create_task(append_audit_line(store, payment))
    _pending.add(task)
    task.add_done_callback(_done)
    return payment.invoice_id
