---
type: llm
focus: last_message
criteria: |
  `scripts/replay_orders.py` is the only file of the `scripts` module in `.vibe/modules/scripts.md`, which declares each script an entry point that nothing imports. It imports `main`.

  PASS if no `high` or `medium` severity Orphaned module finding targets the `scripts` module or `scripts/replay_orders.py`.
  FAIL if it is reported at high or medium severity.
weight: 1
---

Does not call a declared script entry point an orphaned module.
