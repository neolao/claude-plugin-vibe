# ledger-service

Rules the modules implement:

- `fees.transfer_fee(amount)`: an outgoing transfer costs 2% of its amount,
  and never more than 5.00.
- `ledger.Ledger.post(amount, memo)`: records one entry; `balance()` sums the
  amounts, `memos()` lists the memos in posting order.
- `tokens.is_expired(token)`: a token is expired once its expiry day has
  passed.
