---
type: llm
focus: last_message
criteria: |
  Every file appears in a `.vibe/modules/*.md` `Files:` list and matches
  its module's role; the imports go controllers → services → repositories
  and fixtures/main.py imports all three, exactly as the map declares; the
  order total is computed once (by the pricing policy) and the repository
  only stores it; fixtures/main.py is the declared wiring entry point.

  PASS if no `high` or `medium` severity Module scope, Circular
  dependency, Layer direction, Responsibility spread, Decision violated or
  Orphaned module finding is reported. A report with no findings at all
  passes.
  FAIL if any is reported at high or medium severity.
weight: 1
---

Invents no cycle, scope drift, spread, decision or orphan in a consistent
layered map.
