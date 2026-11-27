"""Matches imported transactions with open invoices."""


def reconcile(transactions, invoices, window_days=7):
    matched = []
    for transaction in transactions:
        for invoice in invoices:
            if invoice.amount == transaction.amount and invoice.within(transaction.date, window_days):
                matched.append((transaction, invoice))
                break
    return matched
