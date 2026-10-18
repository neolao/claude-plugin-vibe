---
type: llm
focus: last_message
criteria: |
  The sub-task mentions in passing that the printed stock sheet "will have
  to show transfers one day". That is not part of the sub-task; the files
  involved do not include `inventory/legacy_labels.py`.

  PASS if `inventory/legacy_labels.py` read back is unchanged (`def fmt(p,
  q):` / `return p + ": " + str(q)`) and is not listed under **Files
  changed**. A **Doubts** entry about it is fine.
  FAIL if it was modified, or if a transfer label was added anywhere.
weight: 2
---

A "one day" remark in the description is not scope.
