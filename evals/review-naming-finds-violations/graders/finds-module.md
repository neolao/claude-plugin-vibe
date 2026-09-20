---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Module` (or clearly equivalent
  category name) finding pointing at `fixtures/userManager.py`'s file name
  being camelCase while the other files in the same directory
  (`order_processor.py`, `test_order_processor.py`) are snake_case —
  a mixed naming convention across files.
  FAIL if no finding flags this inconsistency.
weight: 1
---

Reports the camelCase `userManager.py` file name against the snake_case
convention used elsewhere as a `Module` finding.
