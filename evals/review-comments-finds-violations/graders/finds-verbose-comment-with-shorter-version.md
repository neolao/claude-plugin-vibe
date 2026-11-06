---
type: llm
focus: last_message
criteria: |
  `withdraw` in fixtures/ledger/accounts.py carries a three-line comment
  ("Note: be careful here, we need to make sure that the withdrawal does
  not take the balance below zero, because an overdraft is not allowed on
  this kind of account, so we raise an error in order to reject the
  operation."). The check and the raise are visible in the code; the only
  information the code does not give is that this kind of account allows no
  overdraft.

  PASS if the reported findings include a `Verbose` or `Partially
  redundant` (or clearly equivalent category name) finding on that comment
  whose SUGGESTION quotes a replacement of at most one line that still says
  no overdraft is allowed on this account (or kind of account).
  FAIL if no finding flags that comment, if the suggestion is to delete it
  outright, or if the suggested replacement drops the no-overdraft rule.
weight: 1
---

Reports the three-line overdraft comment with a one-line replacement that
keeps its only non-obvious information: the shorten step must quote the
short version, and the short version must lose nothing.
