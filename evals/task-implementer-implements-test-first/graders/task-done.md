---
type: llm
focus: last_message
criteria: |
  Judge on the files the workflow read back and the test output it ran:
  1. `inventory/stock.py` has a `remove(product, quantity)` method that
     lowers the level and raises `ValueError` when the quantity exceeds
     the current level (nothing removed in that case);
  2. `tests/test_stock.py` covers a normal removal and a removal that would
     go below zero, in the `unittest` style of the existing tests;
  3. the workflow's own `python3 -m unittest -q` run passed.

  PASS if all three hold.
  FAIL if the method is missing, if going below zero is allowed or
  silently clamped, if a test is missing, or if the workflow's run failed.
weight: 3
---

The sub-task is done as framed, in the project's style, and the workflow's
own re-run confirms it.
