---
type: llm
focus: last_message
criteria: |
  `core/` imports nothing outside itself; `adapters/`, `api/`,
  `notifications/` and `main.py` import inward; `jobs/` imports
  `adapters`. Both ports live in fixtures/core/ports.py, the adapters
  implement them, fixtures/main.py builds and injects them, no adapter
  calls another.

  PASS if no `high` or `medium` severity Circular dependency, Layer
  direction, Port ownership, Leaky port, Adapter purity, Core purity or
  Wiring finding is reported on fixtures/core/, fixtures/adapters/,
  fixtures/api/ or fixtures/main.py. A report with no findings at all
  passes.
  FAIL if any is reported at high or medium severity.
weight: 1
---

Invents no cycle, direction, port or wiring defect in a consistent hexagon.
