"""Nightly runner: one queue of waiting tasks per task type."""
from jobs.queue import enqueue, drain


def schedule_nightly(invoices, exports):
    waiting_invoices = enqueue(("invoice", invoices))
    waiting_exports = enqueue(("export", exports))
    return drain(waiting_invoices), drain(waiting_exports)
