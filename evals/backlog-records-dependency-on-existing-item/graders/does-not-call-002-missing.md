---
type: llm
focus: last_message
criteria: |
  The request named "after 002" and item 002 (`Import Orders From CSV`)
  exists with `status: todo`.

  PASS if the final message presents 002 as a recorded dependency of the new
  item (or does not question it at all), and never says 002 is missing,
  unknown, not found, or was left out.
  FAIL if the message says 002 does not exist or that the dependency was
  dropped.
weight: 2
---

Precision: an existing reference is not mistaken for a missing one.
