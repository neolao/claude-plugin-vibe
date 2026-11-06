---
type: llm
focus: last_message
criteria: |
  Every file appears in a `.vibe/modules/*.md` `Files:` list and matches
  its module's role; fixtures/main.py is the declared entry point and
  imports both modules; `billing` imports `shipping` as declared; the
  invoice is computed once and the delivery fee once; no `.vibe/decisions/`
  exists and the project declares no ports or adapters.

  PASS if no `high` or `medium` severity Module scope, Responsibility
  spread, Orphaned module, Decision violated, Port ownership, Leaky port,
  Adapter purity, Core purity or Wiring finding is reported. A report with
  no findings at all passes.
  FAIL if any is reported at high or medium severity.
weight: 1
---

Invents no drift, orphan, decision or hexagon in a small layered project.
