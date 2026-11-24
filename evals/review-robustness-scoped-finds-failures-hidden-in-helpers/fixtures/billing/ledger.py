from locks.held import held


def post_entry(ledger, entry):
    """Called by the charge and refund flows to record a money movement."""
    with held(ledger.lock):
        ledger.entries.append(entry)
        ledger.balance_cents += entry["cents"]
