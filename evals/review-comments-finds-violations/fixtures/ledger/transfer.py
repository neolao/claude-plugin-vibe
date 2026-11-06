"""Moves money between two accounts; called from the transfer API."""
from datetime import date, timedelta

from ledger.accounts import Account

SETTLEMENT_DELAY = timedelta(days=2)  # business days, settled by the clearing house


def transfer(source: Account, target: Account, amount_cents):
    # withdraw first so a failed withdrawal leaves the target untouched; amount in cents
    source.withdraw(amount_cents)
    target.deposit(amount_cents)
    return date.today() + SETTLEMENT_DELAY
