---
type: llm
focus: last_message
criteria: |
  `adapters` and the composition root `main.py` import from `core`, and
  `main.py` also imports `adapters` — exactly the directions the module map
  declares, and `core` imports neither, so there is no cycle; every file appears in a
  `.vibe/modules/*.md` `Files:` list; `calculate_total` is called from one
  place only; `adapters/config.py` is imported by the gateway.

  PASS if no `high` or `medium` severity Circular dependency, Module scope,
  Responsibility spread, or Orphaned module finding is reported.
  FAIL if any is.
weight: 1
---

Invents no cycle, scope drift, spread concept, or orphan in a consistent module map.
