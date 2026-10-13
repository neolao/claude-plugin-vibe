---
type: llm
focus: last_message
criteria: |
  The dependency directions are `adapters`, `main.py` and `scripts` importing inward (`scripts` imports `main`, `main` imports `adapters` and `core`); `core` imports nothing outside itself. Every file appears in a `.vibe/modules/*.md` `Files:` list.

  PASS if no `high` or `medium` severity Circular dependency, Module scope, or Responsibility spread finding is reported.
  FAIL if it is reported at high or medium severity.
weight: 1
---

Invents no cycle, scope drift, or spread concept in a consistent module map.
