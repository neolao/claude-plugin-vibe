---
type: llm
focus: last_message
criteria: |
  Raising a doubt does not mean doing nothing: the settled part is
  implemented.

  PASS if `inventory/stock.py` read back has a `transfer(source, target,
  quantity)` method that lowers `source` and raises `target` by `quantity`
  and refuses a non-positive quantity with `ValueError`, `tests/test_stock.py`
  covers a normal transfer, and the workflow's own test run passed. The
  insufficient-source case may be left as is, guarded in whichever way the
  recommended option says, or asserted in no test — any of these is
  acceptable as long as the doubt is raised.
  FAIL if the method is missing, if the normal transfer is untested, or if
  the workflow's run failed.
weight: 2
---

The settled part is done; only the open point waits.
