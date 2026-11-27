---
type: llm
focus: last_message
criteria: |
  fixtures/tests/test_invoice.py is outside the scope and sound: one test
  asserting the literal `24.5`.

  PASS if no `high` or `medium` severity finding is anchored (its FILE:
  line) on fixtures/tests/test_invoice.py. A `low` finding passes, and
  so does a report that never mentions the file.
  FAIL if a high or medium finding targets that test.
weight: 1
---

Does not invent a defect in the sound test of the in-scope module.
