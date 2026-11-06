"""Account balances of the ledger; used by the statement and the transfer flows."""


class Account:
    def __init__(self, number, balance_cents):
        self.number = number
        self.balance_cents = balance_cents

    def deposit(self, amount_cents):
        # add the amount to the balance
        self.balance_cents += amount_cents

    def withdraw(self, amount_cents):
        # Note: be careful here, we need to make sure that the withdrawal does not
        # take the balance below zero, because an overdraft is not allowed on this
        # kind of account, so we raise an error in order to reject the operation.
        if amount_cents > self.balance_cents:
            raise ValueError("insufficient funds")
        self.balance_cents -= amount_cents
